#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: 数据结构与算法
# Author: zcj
# @Time: 2019/8/28 14:05

from timeit import Timer

def test1():
    li = []
    for i in range(1000):
        li = li + [i]

def test2():
    li = []
    for i in range(1000):
        li.append(i)

def test3():
    li = [i for i in range(1000)]

def test4():
    li = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number = 1000), "seconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number = 1000), "seconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number = 1000), "seconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number = 1000), "seconds")

'''
结果：concat 1.3353235 seconds
      append 0.07468719999999984 seconds
      comprehension 0.03133909999999984 seconds
      list range 0.013042100000000056 seconds
'''

#pop测试

a = [i for i in range(2000000)]
pop_zero = Timer("a.pop(0)", "from __main__ import a")
print("pop_zero", pop_zero.timeit(number = 1000), "seconds")

pop_end = Timer("a.pop()", "from __main__ import a")
print("pop_end", pop_end.timeit(number = 1000), "seconds")

list_append = Timer("a.append(1)", "from __main__ import a" )
print("list_append(从后插入)", list_append.timeit(number = 1000), "senconds")

list_insert = Timer("a.insert(0, 1)", "from __main__ import a")
print("lsit_insert(从前插入)", list_insert.timeit(number = 1000), "seconds")

'''
结果：
pop_zero 1.2265271 seconds
pop_end 9.5200000000073e-05 seconds
list_append(从后插入) 5.540000000037182e-05 senconds
lsit_insert(从前插入) 1.5397156000000005 seconds
'''
