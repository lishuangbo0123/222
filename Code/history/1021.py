# 李双博
# 学习python
# 开发时间 2021/10/21  17:11
# import random
import random

#
# ran = random.randint(1, 50)
# while True:
#     guess = int(input('请输入随机数组：'))
#     if guess == ran:
#         print('恭喜你，猜对了')
#         break
#     elif guess > ran:
#         print('猜大了，小一点')
#     elif guess < ran:
#         print('猜小了，大一点')
# for i in range(0, 10):{
#     print(i)
# }
# import random
#
# money = 1
# count = 0
# while True:
#     if money < 5:
#         print('当前金币为%d金币不足，请充值' % money)
#         result = input('是否要充值:(N/Y)')
#         if result == 'N':
#             print('不充值，没钱玩游戏结束')
#             print('当前金币：%d 当前游戏次数%d' % (money, count))
#             break
#         elif result == 'Y':
#             money += int(input('请输入充值金额:')) * 2
#     else:
#         print('开始游戏')
#         money -= 5
#         print('消耗5个金币，当前金币%d' % money)
#         money += 1
#         print('获赠1妹金币,当前金币%d' % money)
#         count += 1
#         guess1 = random.randint(1, 6)
#         guess2 = random.randint(1, 6)
#         print('你摇的点数是%d' % guess1)
#         maxOrMin = input('请猜大小：（D/X）')
#
#         if (maxOrMin == 'D' and (guess1 + guess2) > 6) or maxOrMin == 'X' and (guess1 + guess2) <= 6:
#             print('你赢了')
#             money += 2
#
#             print('奖励两枚金币，当前金币%d' % money)
#             isGo = input('是否继续：（Y/N）')
#             if isGo == 'N':
#                 print('当前金币：%d 当前游戏次数%d' % (money, count))
#                 break
#
#         else:
#             print('你输了')
#             isGo = input('是否继续：（Y/N）')
#             if isGo == 'N':
#                 print('当前金币：%d 当前游戏次数%d' % (money, count))
#                 break


# s = 'ABCDEFG'
# a = '0123456'
# b = '7654321'
# print(s[-1:-7:-2])

# s = 'abcss1b23'
# print(len(s))
# print(s.rfind('1' [3: 5]))
# z= chr(100)
# print(z)
# list = ['酸奶','辣条', '酸奶', '酸奶', '苹果']
# while True:
#     if '酸奶' in list:
#         list.remove('酸奶')
#     else:
#         break
# list1 = ['辣条', '酸奶', '酸奶', '苹果']
# for i in list:
#     if i == '酸奶':
#         list1.remove(i)

# print(list)
# print('*'*20)
# print(list1)
# list = ['酸奶','辣条', '酸奶', '酸奶', '苹果']
# for i in list[::1]:
# for i in list[::1]:
#     if i == '酸奶':
#         list.remove('酸奶')
#
# print(list)
list1 = [1,2,3]
list2 = list1
del list1
print(list2)