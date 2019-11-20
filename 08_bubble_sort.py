#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/14 10:50

#按照升序，从小到大的顺序

# for i in range(6):
#     print(i)           # i: 0到5

# for i in range(10, 0, -1):
#     print(i)             # i: 10到1

#range() 函数左闭右开
"""
重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

步骤：比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
      对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
      针对所有的元素重复以上的步骤，除了最后一个。
      持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for i in range(n - 1, 0, -1):
        # i表示每次遍历需要比较的次数，是逐渐减小的
        # i: n-1, n-2, ... ,1
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def bubble_sort1(alist):
    """冒泡排序，用顺序表实现"""
    n = len(alist)
    #第一层循环用来控制趟数，也就是重复遍历的次数
    for j in range(n - 1):
        # j  从0到n-2
        # 第二层循环就是进行一次遍历，比较前后两个数的大小(也就是所谓的一趟)
        # for i in range(n - 1):
        for i in range(n - 1 - j):
            # i: 0到n-2
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def bubble_sort2(alist):
    """冒泡排序，用顺序表实现"""
    n = len(alist)
    #第一层循环用来控制趟数，也就是重复遍历的次数
    for j in range(n - 1):
        count = 0
        # j  从0到n-2
        # 第二层循环就是进行一次遍历，比较前后两个数的大小(也就是所谓的一趟)
        # for i in range(n - 1):
        for i in range(n - 1 - j):
            # i: 0到n-2
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            break
"""
总共要进行n-1趟

第 1 趟      比较 n-1 次 
第 2 趟      比较 n-2 次 
第 3 趟      比较 n-3 次 
...
第 n-1 趟    比较 1 次 
"""
"""
j             i
0(第一趟)     0: n-2     rang(n-1)    rang(n-1-0) 
1(第二趟)     0: n-3     rang(n-2)    rang(n-1-1) 
2(第三趟)     0: n-4     rang(n-3)    rang(n-1-2) 
...
"""
"""
最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n^2)
稳定性：稳定
"""
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    # bubble_sort1(li)
    print(li)

    l = [1, 2, 3, 4, 5, 6]
    bubble_sort2(l)                      # 时间复杂度为O(n)
    print(l)


