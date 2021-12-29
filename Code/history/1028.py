# 李双博
# 学习python
# 开发时间 2021/10/28  12:08
# class TheFirstDemo:
#     name = 'hello world'
#     def __init__(self):
#         print(f'name is :helleo')
#
#
#
#
# zhangsan = TheFirstDemo()

# class Person:
#     def __init__(self):
#         print((self))
#
#     def study(self,name):
#         print(f'{name} 正在学习')


# person = Person()
# # print(type(person))
# # person.name = '张三'
# # person.study(person.name)
# aa = person.study
# aa("name")


# class Person:
#     def who(self):
#         print(self)
# zhangsan = Person()
# #第一种方式
# zhangsan.who()
# #第二种方式
# who = zhangsan.who
# who()#通过 who 变量调用zhangsan对象中的 who() 方法

# a = 6
# print(id(a))
# a=7
# print(id(a))
#
# b = ['a','b']
# print(id(b))
# b.append('c')
# print(id(b))

def ceshi(*args, **kwargs):

    print(args, kwargs)

if __name__ == '__main__':
    a = 1
    b =2
    ceshi(1, 2, 3, "a", a=1,b=2)
