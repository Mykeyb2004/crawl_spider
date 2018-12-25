import json

str = ''
with open('taobao.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
cookie = [item["name"] + "=" + item["value"] for item in listCookies]
cookiestr = '; '.join(item for item in cookie)
print(cookiestr)
