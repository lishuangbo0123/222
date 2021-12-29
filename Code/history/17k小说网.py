# 李双博
# 学习python
# 开发时间 2021/12/23  13:40
import requests
url = 'https://passport.17k.com/ck/user/login'
session = requests.session()
data = {
    'loginName': '15005010623',
    'password': 'Niyingle@54321'
}
resp = session.post(url,data = data)
# print(resp.json())
url_shelf = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
resp1 = session.get(url_shelf)
print(resp1.json())