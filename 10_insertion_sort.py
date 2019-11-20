#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/16 0:17
"""
通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，
在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""
# a = [93, 54, 77, 31, 44, 55, 26]
# a = [93,       54, 77, 31, 44, 55, 26]
# a = [54, 93,       77, 31, 44, 55, 26]
# a = [54, 77, 93,     31, 44, 55, 26]
#先假定列表中的第一个元素是有序的，从第二个开始，取出第二个与前面的有序表进行比较、插入到合适的位置
def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # j: 1到n-1
        #j 用来控制无序区的第一个元素
        i = j
        #执行从右边的无序序列中取出第一个元素，即i的位置，然后将其插入到前面有序序列的合适位置
        while(i > 0):
            # i是无序区的第一个元素，i-1是有序区的最后一个元素， i -= 1是对无序区从后往前遍历
            if alist[i] < alist[i - 1]:
                alist[i - 1], alist[i] = alist[i], alist[i - 1]
                i -= 1
            else:
                break

def insert_sort1(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # j: 1到n-1
        #j 用来控制无序区的第一个元素
        i = j
        #执行从右边的无序序列中取出第一个元素，即i的位置，然后将其插入到前面有序序列的合适位置
        for k in range(i, 0, -1):
            # i是无序区的第一个元素，i-1是有序区的最后一个元素， i -= 1是对无序区从后往前遍历
            if alist[k] < alist[k - 1]:
                alist[k - 1], alist[k] = alist[k], alist[k - 1]
            else:
                break
"""
最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n2)
稳定性：稳定
"""
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)
    insert_sort1(li)
    print(li)