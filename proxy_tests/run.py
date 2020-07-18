import requests

#testing proxy on url and returning proxies that work
def test_proxy(proxy,url):
    host = proxy[0]
    port = proxy[1]
    username = proxy[2]
    password = proxy[3]

    proxy_argument = {'https': f'https://{username}:{password}@{host}:{port}'}
    try:
        r = requests.get(f'https://{url}', proxies=proxy_argument, timeout=3.5)
        return proxy
    except requests.exceptions.ProxyError:
        print(f'{proxy} Banned on {url}')


URL = "tahjir.com"

file_data = open("proxy_data","r").read()
file_data = file_data.split('\n')
proxies = []
for i in file_data:
    proxies.append(i.split(":"))
working_proxies = []
for proxy in proxies:
    working_proxies.append(test_proxy(proxy,URL))

print(working_proxies)
