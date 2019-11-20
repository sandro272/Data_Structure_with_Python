#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/16 10:30

#>>> 6/2
#3.0
#>>> type(6/3)
#<class 'float'>
#>>> 6//2
#3
#>>> 3//2
#1

def shell_sort1(alist):
    """希尔排序, 希尔排序(Shell Sort)是插入排序的一种"""
    n = len(alist)
    # gap是步长
    gap = n // 2

    # i = 4
    # if alist[i] < alist[i - gap]:
    #     alist[i], alist[i - gap] = alist[i - gap], alist[i]
    while gap > 0:
        # 希尔排序与插入排序的区别就是gap(步长)，当希尔排序的步长等于1是则变成了插入排序
        for j in range(gap, n):
            # j: gap, gap+1, gap+2, ..., n-1
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:                             # alist[8] < alist[4]
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]   # alist[8]和alist[4]互换
                    #当 i=8 时，发现alist[8] < alist[4]， alist[8]和alist[4]互换，但是互换后又发现 alist[4] < alist[0]，故又往前进行一次收缩比较
                    i -= 1
                else:
                    break

        # 缩短gap的步长
        gap //= 2


def shell_sort(alist):

    n = len(alist)
    gap = n // 2
    while gap > 0:
        # gap从1开始
        for j in range(gap, n):
            i = j
            # i = 8
            while i >= gap:
                if alist[i] < alist [i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist [i]
                    i -= gap
                else:
                    break
        gap //= 2


"""
最优时间复杂度：根据步长序列的不同而不同
最坏时间复杂度：O(n2)
稳定想：不稳定
"""

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort1(li)
    print(li)
    shell_sort(li)
    print(li)