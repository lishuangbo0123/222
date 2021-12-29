# 李双博
# 学习python
# 开发时间 2021/12/14  9:48
# class Person:
#
# @classmethod
# def func(self):
#     pass
# def __init__(self):
#     pass

class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__score = 59
    def __str__(self):
        return str(self.__age) + 'de '+self.__name + '考了'+str(self.__score)+'fen'
    def setAge(self,age):
        if 0 < age <120:
            self.__age = age
        else:
            print('年龄不符')
    def getAge(self):
        pass




s = Student('aaa',18)
s.setAge(2000)
print(dir(Student))

