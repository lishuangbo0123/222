# 李双博
# 学习python
# 开发时间 2021/12/21  16:56

import re

# findall  匹配所有结果返回一个list
list7 = re.findall(r'\d+', '我的电话是:10086,你的电话是10010')
print(type(list7))
for i in list7:
    print(i)

# finditer  匹配所有结果返回一个迭代器，迭代器里面是match对象，使用group()函数才能查看结果
list1 = re.finditer(r'\d+', '我的电话是:10086,你的电话是10010')
print(type(list1))
for i in list1:
    print(type(i))
    print(i.group())

# search 返回一个match对象，匹配到一个结果就停止，查看需需用group()函数
list2 = re.search(r'\d+', '我的电话是:10086,你的电话是10010')
print(type(list2))
print(list2.group())

# match   从头开始匹配，如果没有就返回None，返回的是一个match对象,查看需用group()函数
list3 = re.match(r'\d+', '10086,你的电话是10010')
print(list3)

# 预加载正则表达式  好处是可以反复是使用此正则
obj = re.compile(r'\d+')
list9 = obj.findall('我的电话是:10086,你的电话是10010')
print(list9)
s = '''
<div class='jay'><span id = '1'>郭麒麟</span></div>
<div class='jj'><span id = '2'>大聪明</span></div>
<div class='jony'><span id = '3'>卧龙</span></div>
<div class='lisa'><span id = '4'>凤雏</span></div>
<div class='tom'><span id = '5'>大忽悠</span></div>
'''
# re.S的作用是让*可以匹配任意字符
obj = re.compile(r"<div class='.*?'><span id = '(?P<id>.*?)'>(?P<name>.*?)</span></div>",re.S)
iter1 = obj.finditer(s)
for i in iter1:
    print(i.group('id'))
    print(i.group('name'))

