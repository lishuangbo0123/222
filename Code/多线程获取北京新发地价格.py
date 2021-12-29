# 李双博
# 学习python
# 开发时间 2021/12/24  14:37
import requests
import csv
from concurrent.futures import ThreadPoolExecutor
import time
import json

def get_one_page_data(url, page):
    data = {
        "limit": "",
        "current": page,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""
    }
    resp = requests.post(url, data=data)
    dic = dict(resp.json())
    list1 = dic['list']

    f = open('history/xfd.csv', mode='a', encoding='utf-8')
    csvwriter = csv.writer(f)
    for i in list1:
        prodName = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        place = i['place']
        pubDate = i['pubDate']
        txt = [prodName,lowPrice,highPrice,place,pubDate]

        print(txt)
        csvwriter.writerow(txt)




if __name__ == '__main__':
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    # t1 = time.time()
    # print(t1)

    with ThreadPoolExecutor(50) as t:
        for i in range(1, 100):
            t.submit(get_one_page_data,url = url,page = i)  #这种才是多线程
            # t.submit(get_one_page_data, url, i) #这种才是多线程
            # t.submit(get_one_page_data(url=url, page=i))  这种写法不是多线程，这仍然是单线程，很耗时
    # t2 = time.time()
    # print(t2)
    # print(t2-t1)
