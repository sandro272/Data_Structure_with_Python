#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/12 11:42

class DoubleNode(object):
    '''双向链表的节点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prior = None

class DoubleLinkList(object):
    '''双向链表'''
    def __init__(self, double_node = None):
        self.__head = double_node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head is None


    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next
        print("")


    def add(self, item):
        '''链表头部添加'''
        node = DoubleNode(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self.__head
            # 将_head的头节点的prev指向node
            self.__head.prior = node
            # 将_head 指向node
            self.__head = node


    def append(self, item):
        '''链表尾部添加'''
        node = DoubleNode(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            cur = self.__head
            # 移动到链表尾部
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prior = cur



    def insert(self, pos, item):
        '''指定位置添加
        :param   pos从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = DoubleNode(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prior = cur.prior
            cur.prior.next = node
            cur.prior = node




    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #如果要删除的是链表的第一个节点
                if cur == self.__head:
                    self.__head =  cur.next
                    # 判断链表是否仅有一个节点
                    if cur.next:
                        cur.next.prior = None
                else:
                    cur.prior.next = cur.next
                    if cur.next:
                        cur.next.prior  = cur.prior
                break
            else:
                cur = cur.next


    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    link = DoubleLinkList()
    print(link.is_empty())           # True
    print(link.length())             # 0

    link.append(1)
    print(link.is_empty())             # False
    print(link.length())              # 1

    link.append(2)
    link.add(8)
    link.insert(-1, 10)
    link.travel()  # 10 8 1 2
    link.insert(0, 15)
    link.travel()  # 15 10 8 1 2
    link.insert(4, 20)
    link.travel()  # 15 10 8 1 20 2
    link.insert(9, 25)
    link.travel()  # 15 10 8 1 20 2 25
    link.insert(7, 30)
    link.travel()  # 15 10 8 1 20 2 25 30
    link.append(3)
    link.append(4)
    link.append(5)
    link.travel()  # 15 10 8 1 20 2 25 30 3 4 5

    print(link.search(100))  # False
    print(link.search(20))  # True

    link.remove(5)
    link.travel()
    link.remove(15)
    link.travel()
    link.remove(1)
    link.travel()
