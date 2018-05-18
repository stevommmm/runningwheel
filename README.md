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
```
Processing /tmp/httpie-0.9.9-py2.py3-none-any.whl
Collecting requests>=2.11.0 (from httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl (88kB)
Collecting Pygments>=2.1.3 (from httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/02/ee/b6e02dc6529e82b75bb06823ff7d005b141037cb1416b10c6f00fc419dca/Pygments-2.2.0-py2.py3-none-any.whl (841kB)
Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.11.0->httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
Collecting certifi>=2017.4.17 (from requests>=2.11.0->httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/7c/e6/92ad559b7192d846975fc916b65f667c7b8c3a32bea7372340bfe9a15fa5/certifi-2018.4.16-py2.py3-none-any.whl (150kB)
Collecting urllib3<1.23,>=1.21.1 (from requests>=2.11.0->httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/63/cb/6965947c13a94236f6d4b8223e21beb4d576dc72e8130bd7880f600839b8/urllib3-1.22-py2.py3-none-any.whl (132kB)
Collecting idna<2.7,>=2.5 (from requests>=2.11.0->httpie==0.9.9)
Downloading https://files.pythonhosted.org/packages/27/cc/6dd9a3869f15c2edfab863b992838277279ce92663d334df9ecf5106f5c6/idna-2.6-py2.py3-none-any.whl (56kB)
Installing collected packages: chardet, certifi, urllib3, idna, requests, Pygments, httpie
Successfully installed Pygments-2.2.0 certifi-2018.4.16 chardet-3.0.4 httpie-0.9.9 idna-2.6 requests-2.18.4 urllib3-1.22
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com.au/">here</A>.
</BODY></HTML>
```