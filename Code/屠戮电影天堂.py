# 李双博
# 学习python
# 开发时间 2021/12/21  19:33
import csv
import requests
import re
url = 'https://www.dydytt.net/index2.htm'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"}
resp = requests.get(url,headers=headers)
# resp.encoding = 'gb2312'
# print(resp.request.headers)
result = resp.content.decode('gb2312')
# result = resp.text
#resp.text 请求到的是字符串 resp.content请求到的是字节 字节转化成字符串是解码，反之是编码
#resp.encoding 本质是将请求到的字节以某种方式进行解码  和 resp.content.decode()是一样的效果
obj = re.compile(r'''2021新片精品(?P<content>.*?)<!--\{start:迅雷电影下载-->''',re.S)
child_obj = re.compile(r"最新电影下载</a>]<a href='(?P<url>.*?)'>(?P<name>.*?)</a><br/>",re.S)
r = obj.finditer(result)
request_list = []
for i in r:
    dic = i.groupdict()
    child_result = dic['content']
    for j in child_obj.finditer(child_result):
        child_dic = j.groupdict()
        # print(child_dic)
        request_list.append(child_dic)


url_pre = 'https://www.dydytt.net'
f = open('history/download.csv', mode='w', encoding='utf-8')
csv_writer =csv.writer(f)
download_obj = re.compile(r'br /><br /><br /><a target="_blank" href="(?P<download>.*?)"><strong>',re.S)
for i in request_list:
    s = url_pre + i['url']
    resp = requests.get(s,headers=headers)
    resp.encoding = 'gb2312'
    s_result = resp.text
    # print(s_result)
    download_url = download_obj.finditer(s_result)
    for j in download_url:
        s_dic = j.groupdict()
        s_dic['name'] = i['name']
        csv_writer.writerow(s_dic.values())
# print(s_list)
f.close()
resp.close()