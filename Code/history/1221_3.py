# 李双博
# 学习python
# 开发时间 2021/12/21  14:41
import requests
url = 'https://movie.douban.com/j/chart/top_list'
param = {
    "type": "13",
    "interval_id": "100:90",
    "action":"",
    "start": 0,
    "limit": 20
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
}
resp = requests.get(url,params=param,headers=headers)
resp.close()
# print(resp.request.headers)
print(resp.json())
