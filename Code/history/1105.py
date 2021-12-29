# 李双博
# 学习python
# 开发时间 2021/11/5  13:10

# def register():
#     username = input('请输入用户名：')
#     if len(username) < 6:
#         raise Exception('用户名不能小于6位')
#     return print(111)
#
#
# try:
#     register()
# except Exception as err:
#     print(err)
# else:
#     print('成功')
# finally:
#     print('无论如何都会走')

#
# print('dsa')
# names = ['tom','lili','abc','jack','steven','bob','ha']
# filter = filter(lambda x:len(x)>3,names)
# print(list(filter))
#
# result = [i for i in range(101) if i%3==0]
# print(result)


#
# result = [(i,j) for i in range(5) if i%2==0 for j in range(10) if j %2==1]
# print(result)
#
# # list1 = [[1,2,3],[4,5,6],[7,8,9]]
# # result = [i[-1] for i in list1 ]
# # print(result)
#
# dict1 = {'name': 'a', 'salary': 4000}
# dict2 = {'name': 'b', 'salary': 5000}
# dict3 = {'name': 'c', 'salary': 6000}
# dict4 = {'name': 'd', 'salary': 7000}
# list1 = [dict1, dict2, dict3, dict4]
# # result = [{'name':i['name'],'salary':i['salary']+200} if i['salary']>5000 else {'name':i['name'],'salary':i['salary']+500} for i in list1]
# #
# print(list1)


# newlist = [i*3 for i in range(100)]
# print(newlist)
# g = (i*3 for i in range(100))
# while True:
#     try:
#         a = next(g)
#         print(a)
#     except:
#         break

# def fun():
#     n = 0
#     while True:
#         n += 1
#         # print(n)
#         yield n #等效于return+暂停
# print(type(fun()))
# g = fun() #这句话一定要写，用变量去接收生成器，使g的地址时固定的，否则直接用next(func())那么fun()的地址时一直变化的，故每次拿到的值都是1
# a = fun()
# print(id(g),id(a))
# print(next(g))
# print(next(g))
# print(g.__next__())
# print(next(g))
# print(g.__next__())
# print(next(g))
# print(g.__next__())

def fib(length):
    a,b = 0,1
    n = 0
    while n < length:
        a,b = b,a+b
        n+=1
        # print(n)
        temp = yield a
        print('temp:',temp)
        for x in range(temp):
            print(a)

g = fib(100)

print(g.send(None))
print(g.send(1))
print(g.send(2))
print(g.send(3))















