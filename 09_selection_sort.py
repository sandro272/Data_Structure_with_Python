#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/14 16:43

"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""

# a = [54, 226, 93, 17, 77, 31, 44, 55, 20]
#       0,  1,   2,  3,  4,  5,  6,  7,  8

#一开始设定 min = 0, 往后走发现3比0小，故把 min = 3,...
# a[0], a[3] = a[3], a[0]

# a = [17,    226, 93, 54, 77, 31, 44, 55, 20]
#       0,     1,   2,  3,  4,  5,  6,  7,  8
# min=1 -> min=2 -> min=3 -> ... -> min=8
# a[1], a[8] = a[8], a[1]

"""
先写内部循环，也就是一趟排序，在写外部循环
"""

def selection_sort(alist):
    """选择排序"""
    n = len(alist)
    #最初假设最小值所在的位置0索引
    # min_index = 0
    #从索引1往后遍历，如果找到比索引0还小的数，就交换
    # for i in range(1, n):
    #     if alist[min_index] > alist[i]:
    #         min_index = i
    # alist[0], alist[min_index] = alist[min_index], alist[0]

    #j: 0～n-2
    for j in range(n-1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

"""
最优时间复杂度：O(n2)
最坏时间复杂度：O(n2)
稳定性：不稳定（考虑升序每次选择最大的情况）
"""
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(li)
    print(li)