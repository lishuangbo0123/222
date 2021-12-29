# 李双博
# 学习python
# 开发时间 2021/12/23  15:06

import requests
# 免费代理ip  百度搜索https://www.89ip.cn/
ip = '47.243.107.17'
port = '59394'
proxies = {
    'https' : 'https://'+ip+':'+port
}
url = 'https://www.baidu.com/'
print(proxies)
resp = requests.get(url,proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
resp.close()
