import requests
url = 'http://www.baidu.com'
resp = requests.get(url)
print(resp)
print(resp.text)