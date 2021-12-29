# 李双博
# 学习python
# 开发时间 2021/12/20  15:20
import random


class Road:
    def __init__(self,roadName,len):
        self.__roadName = roadName
        self.__len = len
    @property
    def roadName(self):
        return  self.__roadName
    @roadName.setter
    def roadName(self,roadName):
        self.__roadName = roadName

class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed

    def get_time(self,road):
        ran_time = random.randint(1,10)
        msg = '{}品牌的车，在{}路上行驶了{}小时'.format(self.__brand,road.roadName,ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车速度是{}'.format(self.__brand,self.__speed)

road = Road('双桥',250)
print(road.roadName)
road.roadName = 'liusha'
print(road.roadName)
car1 = Car('奔驰','250')
car1.get_time(road)