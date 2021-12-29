# 李双博
# 学习python
# 开发时间 2021/12/23  14:15

import requests
url = 'https://www.pearvideo.com/video_1717772'
cont_id = url.split('_')[-1]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
    "Referer": url
}
url_1 = f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=0.30147982767508763'
# https://video.pearvideo.com/mp4/adshort/20210123/1640240230632-15585850_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20210123/cont-1717772-15585850_adpkg-ad_hd.mp4
session = requests.session()
resp = session.get(url_1,headers = headers)
# print(resp.json())
dic = resp.json()
systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']
video_url = srcUrl.replace(systemTime,'cont-'+cont_id)
print(video_url)
video = requests.get(video_url).content
video_name = video_url.split('/')[-1]
with open('imgimg/'+video_name,mode = 'wb') as f:
    f.write(video)
    print('over')


