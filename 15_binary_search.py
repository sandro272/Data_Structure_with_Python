#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/19 16:16

"""
优点是比较次数少，查找速度快，平均性能好；其缺点是要求待查表为有序表，
且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。
"""
"""
进行索引引用时，需要弄清楚是要在原始的数据集合(比如原始的顺序表中)中对数据进行查找，
还是从原始的数据集合中取出一部分数据组成一个新的数据集合，
"""

def binary_search1(alist, item):
    """二分查找, 递归版本"""

    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search1(alist[: mid], item)
        else:
            return binary_search1(alist[mid + 1:], item)
    # else:
    #     return False
    return  False


def binary_search(alist, item):
    """二分查找， 非递归形式"""
    n = len(alist)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

"""
最优时间复杂度：O(1)
最坏时间复杂度：O(logn)
"""
if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    res = binary_search1(li, 100)
    print(res)
    print(binary_search(li, 31))




