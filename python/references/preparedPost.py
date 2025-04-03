from requests import Request, Session

s = Session()

req = Request('POST', 'https://httpbin.org/post', data='data', headers={'Content-Type': 'application/json'})
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    stream=None,
    verify=True,
    proxies=None,
    cert=None,
    timeout=1
)

print(resp.status_code)