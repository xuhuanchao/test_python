# -*- coding: UTF-8 -*-
# !/usr/bin/python3
import keyword


print("hello , world")

# 关键字
print(keyword.kwlist)


# 注释

# 单行注释

'''
多行注释
'''

"""
多行注释
"""

# 行锁进，可以不用{}
if True:
    print(1)
    print(2)
else:
    print(3)


# 一行语句换行使用 \
total = 1 + 2 + \
    3 + 4
print(total)


# 数字类型Number，整型、布尔型、浮点数、复数
'''
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''


# String 字符串
'''
python中单引号和双引号使用完全相同。
使用三引号(\'\'\'或\"\"\")可以指定一个多行字符串。
转义符  \
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标]
'''

word = 'some word'
sentence = 'asd saef'
paragraph = '''afaf
asdfafd'''

print(word)
print(word[0:-1])
print(word[5:] + '555')
print(word[-1])
print(word[2:5])


# 等待用户输入
#input("\n\n按下 enter 键后退出。")

# 同一行多条语句用；隔开
a = 1; b = a+2; print(b)


# 代码组
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
'''
print('代码组：')
test = 1;
if test == 1:
    print(test)
elif test == 2:
    test = test + 1;
    print(test)
else:
    test = 0
    print(test)


# print输出
'''
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''
x = "a"
y = "b"
print(x)
print(y)
print('-------')
print(x, end=" ")
print(y, end=" ")
print()


# import \ from import
'''
import somemodule
from somemodule import somefunction
from somemodule import firstfunc, secondfunc, thirdfunc
from somemodule import *
'''

import sys
print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


# 命令行参数
'''
python -h


'''