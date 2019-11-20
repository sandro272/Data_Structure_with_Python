#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/18 15:49

"""
采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，
谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
"""

def merge_sort(alist):
    """归并排序，先拆分，在进行合并"""
    n = len(alist)
    #拆分的终止条件
    if n <= 1:
        return alist

    num = n // 2
    # 1//2                 0
    # left 经过归并排序后形成新的有序列表
    left_li = merge_sort(alist[:num])

    # right 经过归并排序后形成新的有序列表
    right_li = merge_sort(alist[num:])

    # 将left_li,right_li两个有序表进行合并
    # merge(left_li, right_li)

    #指针或者游标
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    #把剩余部分添加到result中去
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result
"""
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(nlogn)      执行logn次的n
稳定性：稳定
"""
if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    res = merge_sort(alist)
    print(res)

    """
    执行流程：
    merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        merge_sort([54, 26, 93, 17])
            merge_sort([54, 26])
                merge_sort([54])
                 return [54]
                merge_sort([26)
                 return [26]
            return [26,54]
            merge_sort([93, 17])
                merge_sort([93])
                 return [93]
                merge_sort([17)
                 return [17]
            return [17,93]
        return [17,26,54,93]
        merge_sort([77, 31, 44, 55, 20])
            merge_sort([77, 31])
                merge_sort([77])
                 return [77]
                merge_sort([31)
                 return [31]
            return [31,77]
            merge_sort([44, 55, 20])
                merge_sort([44])
                 return [44]
                merge_sort([55, 20])
                    merge_sort([55])
                     return [55]
                    merge_sort([20])
                     return [20]
                return [20,55]
            return [20,44,55]
        return [20,31,44,55,77]
    return [17, 20, 26, 31, 44, 54, 55, 77, 93]          
    
    """


