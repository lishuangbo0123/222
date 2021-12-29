# 李双博
# 学习python
# 开发时间 2021/12/22  16:28
import requests
from lxml import etree
import csv
url = 'https://quanzhou.zbj.com/search/f/?kw=saas'
resp = requests.get(url)
# print(resp.text)
resp.close()

f = open('history/zhubajie.csv', mode ='w', encoding='utf-8')
csv_writer = csv.writer(f)
html = etree.HTML(resp.text)
root_xpath = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')

for i in root_xpath:
    price = i.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    name = 'saas'.join(i.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
    local = i.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
    com_name = i.xpath('./div/div/a[1]/div[1]/p/text()')[1].strip('')
    # 获取固定标签的数据@href=
    # //代表获取所有后代
    # /@href   代表获取href属性的值
    # /a[@href='dapao']   代表获取a标签且href属性为href的子节点
    csv_writer.writerow([price,name,local,com_name])
f.close()