#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/13 13:02

#python中    0,"",[],(),{}在逻辑值上都为假

'''
l = [1, 2, 3]
print(l)                # [1, 2, 3]
l.append(4)
print(l)               # [1, 2, 3, 4]
l.pop()
print(l)               # [1, 2, 3]
'''

class Stack(object):
    """栈"""
    def __init__(self):
        #使用列表list作为存储容器
        self.__list = []


    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)                      # O(1)
        # self.__list.insert(0, item)                 # 从表的头部插入，时间复杂度等于O(n)


    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()                            # O(1)
        # return self.__list.pop(0)                         # 删除表头元素，时间复杂度等于O(n)


    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            #如果栈不为空
            return self.__list[-1]
        else:
            return None


    def is_empty(self):
        """判断栈是否为空"""
        #空的顺序表在逻辑上属于False
        return self.__list == []
        #return not self.__list


    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())          # True
    s.push(1)
    s.push(2)
    print(s.size())              # 2
    s.push(3)
    s.push(4)
    print(s.peek())             # 4
    print(s.is_empty())         # False
    print(s.pop())             # 4
    print(s.size())                # 3
    print(s.pop())               # 3
    print(s.pop())             # 2
    print(s.pop())             # 1
