# 李双博
# 学习python
# 开发时间 2021/12/21  13:16
from urllib.request import urlopen
url = 'http://www.baidu.com'
resp = urlopen(url)
print(resp.read().decode('utf-8'))
with open('mybaidu.html', mode ='w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
    print('over')