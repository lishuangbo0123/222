# 李双博
# 学习python
# 开发时间 2021/12/21  14:07
import requests
# name  = input('请输入名字')
# url = 'https://www.sogou.com/web?query='+name
# dic = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
# }
# resp = requests.get(url,headers=dic)
# print(resp)
# print(resp.text) #页面源代码
s = input('请输入要翻译的内容')
url = 'https://fanyi.baidu.com/sug'
data = {
    'kw':s
}
resp = requests.post(url,data=data)
print(resp.json())
resp.close()