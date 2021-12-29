# 李双博
# 学习python
# 开发时间 2021/11/17  17:48

from collections.abc import Iterable
# list1 = [1,2,3,4]
# aa = iter(list1)
# print(isinstance(aa,Iterable))
class Phone:
    __name = 'huawei'
    def call(self):
        Phone.__name = 'dasdas'
        print(Phone.__name)



    @classmethod
    def show(cls):
        print(111)
        print(cls.__name)

    def show(self):
        print(222)




phone1 = Phone()
Phone.show()

