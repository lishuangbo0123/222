# 李双博
# 学习python
# 开发时间 2021/11/4  13:12
#

import os

# aa = r'C:\Users\User\Desktop\test1'
# bb = r'C:\Users\User\Desktop\test2'
#
#
# def copyDir(a, b):
#     dir = os.listdir(a)
#     for file in dir:
#         path1 = os.path.join(a, file)
#         if os.path.isdir(path1):
#             path3 = os.path.join(b, file)
#             if not os.path.isdir(path3):
#                 os.mkdir(path3)
#                 copyDir(path1, path3)
#
#         else:
#             print(file)
#             print(b)
#             path2 = os.path.join(b, file)
#             print(path2,type(path2))
#             with open(path1, 'rb') as rstream:
#                 container = rstream.read()
#                 with open(path2, 'wb') as wstream:
#                     wstream.write(container)
#
#     else:
#         print('复制成功')
#
# copyDir(aa,bb)


a = 0
print(id(a))
a= 6
print(id(a))
a= 0
print(id(a))

