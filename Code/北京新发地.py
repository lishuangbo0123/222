import requests
from bs4 import BeautifulSoup

url = 'https://www.dy2018.com/9/'
pre_url = 'https://www.dy2018.com'
resp = requests.get(url)
resp.encoding = 'gb2312'
# print(resp.text)
resp.close()

bs_obj = BeautifulSoup(resp.text,'html.parser')
res1 = bs_obj.find('div',class_ = 'co_area1').find_all('a')
print(res1)
for i in res1:
    print(i.get('href'))

url = 'http://pic.qianye88.com/4kyouxic3064c86-c176-3da2-9e27-9b1ecf507f48.jpg'
img_name = url.split('/')[-1]
print(img_name)
with open('imgimg/' + img_name,mode = 'wb') as f:
    img = requests.get(url)
    f.write(img.content)
    print('over')

