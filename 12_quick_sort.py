#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/16 15:11

"""
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤为：
从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""
# a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# Mid_value = 54
# low = 0
# high = len(a) - 1
# if a[high] > Mid_value:
#     high -= 1
# elif a[high] < Mid_value:
#     a[low] = a[high]
# low += 1
# if a[low] < Mid_value:
#     low += 1
# elif a[low] > Mid_value:
#     a[high] = a[low]
# high -= 1

# a = [1, 2, 3, 4, 5, 6, 7]
# print(id(a))                  # 1805995600328
# print(id(a[0:3]))             # 1805995407112
# print(id(a[5:]))              # 1805995407112   进行切片以后生成一个新的列表

def quick_sort(alist, first, last):
    """插入排序",     对于元素相同的情况下，尽量把相同元素放在一边"""
    # n = len(alist)
    # mid_value = alist[0]
    # low = 0
    # high = n - 1
    low = first
    high = last
    mid_value = alist[first]

    # 递归的退出条件,也就是只有一个元素的时候
    if first >= last:
        return

    #为了使low,high交替进行
    while low < high:
        #最初从右边，也就是high开始
        while low < high and alist[high] >= mid_value:
            # 继续左移
            high -= 1
        alist[low] = alist[high]
        # low += 1

        while low < high and alist[low] < mid_value:
            # 继续右移
            low += 1

        alist[high] = alist[low]
        # high -= 1                       #不要这句只因为当low跟high想遇以后，还会继续错开，因而不要
    # 从循环退出时，low == high
    alist[low] = mid_value
    # 递归    在原始的数据上继续进行排序
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last )

"""
最优时间复杂度：O(nlogn)    n:遍历, logn是划分
最坏时间复杂度：O(n2)       #当划分时，只能分成单只树的形式
稳定性：不稳定
"""

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)