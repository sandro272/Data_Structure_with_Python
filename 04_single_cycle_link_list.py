#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/12 14:22

"""
对于插入和删除操作，先考虑正常情况下（中间）的操作，
然后在考虑特殊情况（比如链表为空，或者只有一个节点，
或者在链表的尾端进行相关操作）
"""
class Node(object):
    '''节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None

class SingleCycleLinkList(object):
    '''单向循环链表'''
    def __init__(self, node = None):
        self.__head = node
        if node is not None:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        # return self.__head == None
        return self.__head is None


    def length(self):
        """"返回链表的长度"""
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            #count记录数量
            count = 1
            while cur.next != self.__head:
                count += 1
                cur = cur.next
        return count


    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end = " ")
            cur = cur.next
        #退出循环，cur指向尾节点，但尾节点的元素并没有打印
        print(cur.elem)


    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            #先进行遍历找到链表尾节点，然后进行插入操作
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = self.__head


    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

            # cur.next = node
            # node.next = self.__head

    def insert(self, pos, item):
        """在指定位置pos添加节点
        :param    pos从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node


    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                #先判断要删除的是否是链表的第一个节点
                if self.__head == cur:
                    #要删除的是链表的第一个节点情况
                    # 先找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 删除的是中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #要删除的是尾节点的情况
        if cur.elem == item:
            if self.__head == cur:
                #链表只有一个节点的情况
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head



    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    singlelist = SingleCycleLinkList()
    print(singlelist.is_empty())  # True
    print(singlelist.length())  # 0

    singlelist.append(1)
    print(singlelist.is_empty())  # False
    print(singlelist.length())  # 1

    singlelist.append(2)
    singlelist.add(8)
    singlelist.insert(-1, 10)
    singlelist.travel()  # 10 8 1 2
    singlelist.insert(0, 15)
    singlelist.travel()  # 15 10 8 1 2
    singlelist.insert(4, 20)
    singlelist.travel()  # 15 10 8 1 20 2
    singlelist.insert(9, 25)
    singlelist.travel()  # 15 10 8 1 20 2 25
    singlelist.insert(7, 30)
    singlelist.travel()  # 15 10 8 1 20 2 25 30
    singlelist.append(3)
    singlelist.append(4)
    singlelist.append(5)
    singlelist.travel()  # 15 10 8 1 20 2 25 30 3 4 5

    print(singlelist.search(100))  # False
    print(singlelist.search(20))  # True

    singlelist.remove(5)
    singlelist.travel()
    singlelist.remove(15)
    singlelist.travel()
    singlelist.remove(1)
    singlelist.travel()