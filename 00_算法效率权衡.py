#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: 数据结构与算法
# Author: zcj
# @Time: 2019/8/21 16:18

import time
"""
题目：如果 a + b + c = 1000, 且 a^2 + b^2 = c^2(a,b,c为自然数)，如何求出所有a,b,c可能的组合
"""
#枚举法    a,b,c一个一个的去试
#思路：a = 0, b = 0, c = 0---1000
#      a = 0, b = 1, c = 0---1000

print("第一次试探")
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a, b, c : (%d, %d, %d)" % (a, b, c))

end_time = time.time()
print("time: " ,end_time - start_time)
print("complete.............first.............")

# T = 1000 * 1000 * 1000 * 2
# T = N * N * N * 2            N是问题的规模
# T(n) = n^3 * 2
# T(n) = n^3 * 10
# T(n) = n^3                   # 29行，30行，31行的T(n)处于同一个数量级

#g(n) = n^3

# T(n) = k * g(n)                # g(n)是T(n)的渐近函数

print("第二次试探")
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c : (%d, %d, %d)" % (a, b, c))

end_time = time.time()
print("time: " ,end_time - start_time)
print("complete............second..............")

# T(n) = n * n * (1 + max(1, 0))         max(1, 0)是否进入循环体，进则为1，否则为0
#      = n^2 * 2
#      = O(n^2)

print("第三次试探")
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c : (%d, %d, %d)" % (a, b, c))

end_time = time.time()
print("time: " ,end_time - start_time)
print("complete............third..............")

# 每台机器执行的总时间不同， 但是执行的基本运算数量大体相同