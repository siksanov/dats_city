from requests import Request, Session

s = Session()
req = Request('GET',  'https://httpbin.org/get', data='data', headers={})

prepped = s.prepare_request(req)

# do something with prepped.body
prepped.body = 'Seriously, send exactly these bytes.'

# do something with prepped.headers
prepped.headers['Keep-Dead'] = 'parrot'

resp = s.send(prepped,
    stream=None,
    verify=True,
    proxies=None,
    cert=None,
    timeout=1
)

print(resp.status_code)