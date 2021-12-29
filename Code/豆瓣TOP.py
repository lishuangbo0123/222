# 李双博
# 学习python
# 开发时间 2021/12/21  18:05
import csv

import requests
import re
import csv
url = 'https://movie.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
}
resp = requests.get(url,headers = headers)
# print(resp.text)

obj = re.compile(r'<span class="title">(?P<nam e>.*?)</span>.*?<span class="title">&nbsp.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>',re.S

)
result = obj.finditer(resp.text)
f = open('history/result.csv', mode='w', encoding='utf-8')
csvwriter = csv.writer(f)
for i in result:
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    print(dic)

    csvwriter.writerow(dic.values())

print('over')
resp.close()