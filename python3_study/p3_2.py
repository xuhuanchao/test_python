# -*- coding: UTF-8 -*-
# !/usr/bin/python3

"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
"""

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)


# 多个变量赋值
'''
将1 赋值给三个变量，指向同一内存
'''
a = b = c = 1
'''
给三个变量分别赋不同的值
'''
a, b, c = 1, 2, "runoob"

# python 6个标准数据类型
'''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
不可变数据（四个）：Number（数字）、String（字符串）、Tuple（元组）、Sets（集合）；
可变数据（两个）：List（列表）、Dictionary（字典）。
'''

# 数字
'''
int
long
float
complex

del var,var2...删除引用
'''

var1 = 10
var2 = 20.3
del var1
print(var2)


# String 字符串
'''
由字母、数字、下划线构成

字符串索引 从左到右 0开始，从右到左-1开始
字符串截取 【开始索引:结束索引】

* 多次输出字符串
+ 连接字符串
'''

print('======= String =======')
s = 'I`m python programer.';
print(s)
print(s[2:])
print(s[2:5])
print(s[-5:-1])
print(s[5:] * 2)
print(s[5:] + 'tttt' * 2)


# 列表 List

print('========== List ========')
list1 = ['zhangsan', '李四', 12, 'ff']
list2 = ['呵呵', 333]
list2 = ['炸弹', 5555]
print(list1)
print(list1 + list2)
print(list1[2:8])


# 元组 Tuple
'''
类似List 但不可修改。用()
'''
print('======  Tuple  ======')
tuple1 = ('大哥', '问候', 45, 'ljgl')
tuple2 = (444, 'fe')
print(tuple1 + tuple2)
print(tuple2 * 3)








