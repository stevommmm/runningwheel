#!/usr/bin/env python3
from aiohttp import web
from pathlib import Path
import aiodocker
import logging

import runningwheel

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
	app = web.Application()
	app['root'] = Path(__file__).parent.absolute()
	app['docker'] = aiodocker.Docker()

	app.router.add_get('/', runningwheel.upload_wheel)
	app.router.add_get('/run/{runtime}', runningwheel.run)
	app.router.add_post('/store', runningwheel.store_wheel)

	app.on_shutdown.append(runningwheel.on_shutdown)

	Path(app['root'], 'wheels/').mkdir(exist_ok=True)
	web.run_app(app)
