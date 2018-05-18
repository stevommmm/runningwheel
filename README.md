# runningwheel

Load in a simple wheel to test
```bash
mkdir -p wheels && pip wheel httpie --no-deps -w ./wheels
```

Run the app, make sure docker is running too
```powershell
$env:DOCKER_HOST='tcp://localhost:2375'
python ./main.py
```


In another terminal:
```bash
curl http://localhost:8080/run/httpie-0.9.9-py2.py3-none-any.whl
```