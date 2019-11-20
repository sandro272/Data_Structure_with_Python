#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/13 23:57

"""  同栈一样，队列也可以用顺序表或者链表实现。"""

class Queue(object):
    """创建一个空的队列"""
    def __init__(self):                         # 构造一个容器用于存储数据
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        # return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())                     # 3
    print(q.dequeue())                  # hello
    print(q.dequeue())                 # world
    print(q.dequeue())                # itcast
