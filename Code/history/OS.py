# 李双博
# 学习python
# 开发时间 2021/11/3  18:47
# import os
from functools import reduce
# C:\Users\User\Desktop\dsadsa.jpg
# with open(r'C:\Users\User\Desktop\dsadsa.jpg', 'rb') as stream:
#     container = stream.read()
#     path1 = os.path.dirname(__file__)
#     print(path1)
#     path2 = stream.name
#     path2 = path2[path2.rfind('\\') +1:]
#     print(path2)
#     path3 = os.path.join(path1, path2)
#     with open(path3, 'wb') as wstream:
#         wstream.write(container)

# list1 = [('a', 12), ('b', 23), ('c', 21)]
# # rr = filter(lambda x:x[1]>20 , list1)
# # print(list(rr))
# rr = reduce(lambda x, y: y**2, [1, 2, 3, 4, 5])
# print(rr)
