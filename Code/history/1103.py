# 李双博
# 学习python
# 开发时间 2021/11/3  17:32

# stream = open(r'C:\Users\User\Desktop\新建文本文档.txt','a')
# C:\Users\User\Desktop\nimg.ws.126.jpg

with open(r'C:\Users\User\Desktop\nimg.ws.126.jpg','rb') as stream:
    container = stream.read()
    with open(r'C:\Users\User\Desktop\dsadsa.jpg','wb') as wstream:
        wstream.write(container)


