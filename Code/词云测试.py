# 李双博
# 学习python
# 开发时间 2021/12/28  23:46

import wordcloud
# 李双博
# 学习python
# 开发时间 2021/12/25  14:20
import requests
import re
import time
from openpyxl import Workbook
import pymysql
import wordcloud


isExcel = True  #是否将数据爬取到excel, 否就把数据存储到数据库
start_excel_line = 2
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Mobile Safari/537.36',
    'Cookie': 'WEIBOCN_FROM=1110005030; SUB=_2A25MwrbpDeRhGeFJ6FAS-CfOzDWIHXVsTNqhrDV6PUJbktCOLXP6kW1NfC2i909AJUiljJkm1hMTtjecoQ-21Doq; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW5FrKPpHKZ.TSeBWE2X70w5JpX5KzhUgL.FoMNe0z01h.ES0.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0eEe0n4eoM4; SSOLoginState=1640416954; MLOGIN=1; BAIDU_SSP_lcr=https://vip.weibo.com/; _T_WM=46971536473; M_WEIBOCN_PARAMS=luicode=10000011&lfid=1076036336553950&fid=1005056336553950&oid=4718396568766801&uicode=10000011; XSRF-TOKEN=db7ada'
}

recomp = re.compile(r'<span.*?</span>', re.S)
recomp1 = re.compile(r'<a.*?</a>', re.S)
# uid = '6336553950' #用户id
uid = '2640705825'  #刘子菡id

page_number = 1 #设置起始页
# containerid = '2304136336553950_-_WEIBO_SECOND_PROFILE_WEIBO'  #容器ID
# id = '4718278381933124'  #文章id
# mid = '4718278381933124'  #文章id


def get_more_containerid(uuid):
    # 根据uid获取容器id
    url = 'https://m.weibo.cn/profile/info?uid='+str(uuid)
    resp = requests.get(url,headers = headers)
    try:
        dic = resp.json()
        print(dic)
    except Exception as err:
        print(err)
        print(url)
        print('有异常')
        resp.close()
        return None

    containerid = dic['data']['more']
    resp.close()
    return containerid

def get_weibo_content(containerid,page,n):
    #获取微博内容 containerid 文章列表id   page是页数  n是第几篇文章

    url = f'https://m.weibo.cn/api/container/getIndex?containerid={containerid}&page_type=03&page=' + str(
        page)

    resp = requests.get(url,headers = headers)

    try:
        dic = resp.json()
        print(dic)
    except Exception as err:
        print('有异常' + str(err))
        print(url,headers)
        resp.close()
        time.sleep(2)
        return None

    content_list = dic['data']['cards']
    for i in content_list:
        if 'mblog' in i.keys():
            text = str(i['mblog']['text'])
            time1 = i['mblog']['created_at']
            msg = '获取第=====================' + str(page) + '======================页数据,第' + str(n) + '篇文章'
            write_data_to(time1, text, '文章',msg,url)
            print(msg)
            comments_count = i['mblog']['comments_count']  # 评论数
            mid = i['mblog']['id']  # 文章id
            if comments_count > 0:
                print('评论数不为0，抓取评论')
                # 评论不为0抓取评论数据
                max_id = ''
                t = 1
                get_weibo_one_hotflow(mid, max_id, page, n, t)
            n += 1
    resp.close()
    time.sleep(2)
    if len(content_list) <=1:
        #无微博了
        return None
    else:
        page += 1
        return get_weibo_content(containerid,page,n)

def get_weibo_one_hotflow(mid,max_id,page,p,t):
    #获取微博1级评论  mid是文章id   max_id是加载到哪里的id   page是页数  p是第几篇文章  t是第几条数据

    url = f'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id_type=0'+max_id
    # print(url)

    resp = requests.get(url,headers = headers)
    try:
        dic = resp.json()
        print(dic)
    except Exception as err:
        print('有异常' + str(err))
        print(url, headers)
        resp.close()
        time.sleep(2)
        return None

    # print(dic)
    if dic['ok'] == 1:
        content_list = dic['data']['data']
        maxid = str(dic['data']['max_id'])  # 用于做判断时用的，如果为0说明是最后一页评论
        max_id = '&max_id=' + maxid  # 用于做参数的max_id

        for i in content_list:
            text = str(i['text'])
            cid = str(i['id'])
            time1 = i['created_at']
            total_number = i['total_number']
            msg = '获取第=====================' + str(page) + '======================页数据,第' + str(p) + '篇文章,第'+ str(t) + '条评论'
            write_data_to(time1, text, '评论',msg,url)
            print(msg)
            if total_number > 0:
                print('子评论数不为0，抓取子评论')
                # 子评论不为0抓取子评论数据
                child_max_id = '&max_id=0'
                z = 1
                get_child_coments(cid, child_max_id,page,p,t,z)
            t += 1
        resp.close()
        time.sleep(2)
        if maxid == '0':
            #无评论
            return None
        else:
            #有评论
            return get_weibo_one_hotflow(mid, max_id,page,p,t)
    else:
        resp.close()
        time.sleep(2)
        return None


def get_child_coments(cid,max_id,page,p,t,z):
    url = f'https://m.weibo.cn/comments/hotFlowChild?cid={cid}&max_id_type=0'+max_id
    # print(url)
    resp = requests.get(url, headers=headers)
    try:
        dic = resp.json()
        print(dic)
    except Exception as err:
        print('有异常'+str(err))
        print(url, headers)
        resp.close()
        time.sleep(2)
        return None

    # print(dic)
    if dic['ok'] == 1:
        content_list = dic['data']
        maxid = str(dic['max_id'])  # 用于做判断时用的，如果为0说明是最后一页评论
        child_max_id = '&max_id=' + maxid  # 用于做参数的max_id

        for i in content_list:
            text = str(i['text'])
            time1 = i['created_at']
            msg = '获取第=====================' + str(page) + '======================页数据,第' + str(p) + '篇文章,第' + str(t) + '条评论,第'+ str(z) + '条子评论'
            write_data_to(time1, text, '子评论',msg,url)
            print(msg)
            z += 1
        resp.close()
        time.sleep(2)

        if maxid == '0':
            return None
        else:
            return get_child_coments(cid, child_max_id,page,p,t,z)


    else:
        resp.close()
        time.sleep(2)
        return None

def write_data_to(time1,text,type,msg,url):
    text = re.sub(recomp, '', text)
    text = re.sub(recomp1, '', text)
    text = text.replace('<br />', '\n')
    text = text.replace('&quot;', '"')
    # print(text)
    if isExcel:

        global  start_excel_line
        with open('ciyun.txt',mode='a',encoding='utf-8') as f:
            f.write(text+' ')


        start_excel_line += 1
    else:
        cursor = db.cursor()
        print(f"INSERT INTO weibo_content VALUES('{time1}','{text}','{text}','{text}','{url}','{msg}',NULL,1)")
        if type == '文章':
            cursor.execute(f"INSERT INTO weibo_content VALUES('{time1}','{text}',NULL,NULL,'{url}','{msg}',NULL,1)")
        elif type == '评论':
            cursor.execute(f"INSERT INTO weibo_content VALUES('{time1}',NULL,'{text}',NULL,'{url}','{msg}',NULL,1)")
        elif type == '子评论':
            cursor.execute(f"INSERT INTO weibo_content VALUES('{time1}',NULL,NULL,'{text}','{url}','{msg}',NULL,1)")
        db.commit()
        cursor.close()





if __name__ == '__main__':

    containerid = get_more_containerid(uid).replace('/p/','')
    print('containerid===============',containerid)
    # 打开excel用于存储数据
    # if isExcel:
    #     #生成txt文本
    #
    # else:
    #     db = pymysql.connect(user='root',\
    #     password="Niyingle@54321",\
    #     host='36.133.5.196',\
    #     database='pachong_data',\
    #     port=3306,charset='utf8mb4')




    get_weibo_content(containerid,page_number,1)






