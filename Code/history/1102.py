# 李双博
# 学习python
# 开发时间 2021/11/2  13:01

# *args
# **kwargs

# def get_sum(a, b):
#     r = a + b
#     print(r)
#
#
# def get_true_sum(*a):
#     sum = 0
#     for aa in a:
#         sum += aa
#     print(sum)
#
#
# a,*b,c = 1,2,3,4,5
# print(a,b,c)  #1 [2, 3, 4] 5
#
# a,*b,c = 1,5
# print(a,b,c) #1 [] 5

# def showbook(**book):
#     print(book)
#     for k, v in book.items():
#         print(k, v)
#
#
# books = {'作者':'吴承恩', '书名':'aaa'}
#
# showbook(**books)


# result = '-'.join(['a','b','c'])
# print(result)

# def fun():
#     a = [1,23,3]
#     print(id(a))
#     a.append(3)
#     return a
# a = fun()
# print(id(a))


# def get_maxandmin(list1):
#     for j in range(len(list1) - 1):
#         for i in range(len(list1) - 1 - j):
#             if list1[i] > list1[i + 1]:
#                 list1[i], list1[i + 1] = list1[i + 1], list1[i]
#
#     print(list1)
#     return (list1[0],list1[-1])
#
#
# list1= [1, 2, 4, 8, 3, 5, 7]
# result = get_maxandmin(list1)
# print(result)


# a = 100
#
#
# def fun():
#     global a #这样会报错，因为等于a = a + 10试图对函数外的不可变数据进行修改
#     a+=10
#     b = a - 10#如果只有这行代码是可以的，因为没有对函数外的a进行修改，a的值还是100
#     print(b)
#
#
# fun()
# car_park = []
# def go_out():
#     number = input("")
#     for car in car_park:
#         if number in car:


# dic = {'a': 1, 'b': 2, 'c': 3}
# result = dic.get('a')
# print(result)
# str = 'hahaha,%(a)shehenduo%(b)s'
# print(str % dic)

# def fun():
#     '''
#     hdsa
#     :rtype: str
#     :return:
#     '''
# help(fun())
# a = (1,2)
# a += (3,4,5)
# print(a)

# import sys
# list1 = [1,2,3,4,5]
# b = list1
# c = b
# print(sys.getrefcount(list1))
# def test(n1):
#     print(id(n1))
#     n1+=1
#     print(id(n1))
#
# n = 9
# print(id(n))
# test(n)

# def outer():
#     a = 100
#     def inner():
#         b =200
#         print('我是内部函数')
#     print(locals())
#
#
# outer()
# import sys
#
# list = [1,2,3]
# list1 = list
# list2 = list
# print(sys.getrefcount(list))
# def fun(l):
#     print(sys.getrefcount(l))
#     print(sys.getrefcount(list))
#     list3 = l
#     print(sys.getrefcount(l))
#
# fun(list)
# print(sys.getrefcount(list))


# def newfun(fun):
#
#     def ret():
#         fun()
#         print('新功能')
#     return ret
#
# @newfun # house =newfun(house)
# def house():
#     print('毛坯房')
#
#
# house()


def fun(i):
    if i == 1 or i == 2:
        return 1
    return fun(i-1) + fun(i-2)

print(fun(5))