import requests
from seleniumwire import webdriver

#testing proxy on url and returning proxies that work
def test_proxy(proxy,url,page_title,use_request=False):
    host = proxy[0]
    port = proxy[1]
    username = proxy[2]
    password = proxy[3]

    if use_request == True:
        proxy_argument = {'https': f'https://{username}:{password}@{host}:{port}'}
        try:
            print("Testing proxy")
            r = requests.get(f'https://{url}', proxies=proxy_argument, timeout=3.5)
            print('Found working proxy')
            return proxy
        except requests.exceptions.ProxyError:
            print(f'{proxy} Banned on {url}')
    else:
        options = {
            'proxy': {
                'https': f'https://{username}:{password}@{host}:{port}',
            }
        }
        browser = webdriver.Chrome("/Users/CreeperFire/Desktop/PythonT/chromedriver", seleniumwire_options=options)
        try:
            browser.get(url)
            browser.implicitly_wait(5)
            if page_title in browser.title == True:
                return proxy
        except OSError or selenium.common.exceptions.TimeoutException:
            print(proxy,"banned")
        browser.close()

pt = "Supreme"
URL = "https://www.supremenewyork.com/shop/all/sweatshirts"
#1
file_data = open("proxy_data","r").read()
file_data = file_data.split('\n')
proxies = []
for i in file_data:
    proxies.append(i.split(":"))
working_proxies = []
for proxy in proxies:
    working_proxies.append(test_proxy(proxy,URL,pt))

print(working_proxies)