import logging
from pathlib import Path
from aiohttp import web
from aiodocker.exceptions import DockerError
import io
import tarfile

logger = logging.getLogger('runningwheel')
logger.setLevel(logging.DEBUG)


async def upload_wheel(request):
	return web.Response(body='''<form action="/store" method="post" accept-charset="utf-8" enctype="multipart/form-data">

	<label for="wheel">Wheel: </label>
	<input id="wheel" name="wheel" type="file" value=""/>
	<br>
	<input type="submit" value="submit"/>
</form>''', headers={'Content-Type': 'text/html'})


async def run(request):
	runtime = request.match_info['runtime']
	logger.debug(runtime)

	try:
		await request.app['docker'].images.get('python:3.6')
		logger.debug("Found existing image")
	except DockerError:
		logger.info("Pulling missing docker image")
		await request.app['docker'].pull('python:3.6')

	logger.debug("Adding wheel to tarball")
	tario = io.BytesIO()
	tar = tarfile.open(fileobj=tario, mode='w')
	tar.add(Path(request.app['root'], 'wheels/', runtime), arcname=runtime)
	logger.debug("Tar contains %r", tar.getnames())
	tar.close()

	logger.debug("Creating container definition")
	container = await request.app['docker'].containers.create_or_replace(
		config={
			'Cmd': ['/bin/bash', '-c', '/usr/local/bin/pip install /tmp/*.whl && http GET google.com.au'],
			'Image': 'python:3.6',
		},
		name=runtime,
	)
	logger.debug("Injecting wheel to container")
	await container.put_archive(
		path='/tmp',
		data=tario.getvalue()
	)

	await container.start()
	logging.debug(await container.wait())
	logs = await container.log(stdout=True, stderr=True)
	# await container.delete(force=True)
	return web.Response(text='\n'.join(logs))


async def store_wheel(request):
	reader = await request.multipart()

	field = await reader.next()
	logger.debug("Read field %r", field.name)
	if not field.name == 'wheel':
		raise web.HTTPBadRequest()
	filename = field.filename
	if not filename.endswith('.whl'):
		raise web.HTTPBadRequest()

	with Path(request.app['root'], 'wheels/', filename).open('wb') as f:
		while True:
			chunk = await field.read_chunk()
			if not chunk:
				break
			f.write(chunk)
	return web.Response(text='{} successfully stored'''.format(filename))


async def on_shutdown(app):
	await app['docker'].close()