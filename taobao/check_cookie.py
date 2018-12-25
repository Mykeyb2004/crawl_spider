
import requests

url = 'https://i.taobao.com/my_taobao.htm?spm=a21bo.2018.1997525045.1.5af911d9S4MJ92'
cookiestr=''   # YOUR COOKIE RESULT FROM COOKIEGET.PY
headers = {
    'cookie': cookiestr,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

html = requests.get(url=url, headers=headers)

print(html.text)
