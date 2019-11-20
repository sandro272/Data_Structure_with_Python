#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/6 23:59

# python中的 "=" 理解为是一个指向问题

class Node(object):
    """节点"""
    def __init__(self, elem):                   # 构造方法
        self.elem = elem
        self.next = None

# node = Node(100)

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        self.__head = node                           # __head,前面加“__”表示私有方法,自己内部使用知道，不对用户展现


    def is_empty(self):
        """链表是否为空  对象方法"""
        return self.__head == None


    def length1(self):
        """链表长度   对象方法"""
        """cur游标，初始时是指向头节点， 用来移动遍历节点；
           判断链表结束，即链表尾有两种，一种是游标cur移动到None,另外一种是根据cur.next==None
        """
        cur = self.__head                  # 理解为头指针__head指向第一个节点，游标cur也指向第一个节点
        # count用来记录遍历的节点数量
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count


    def length2(self):
        """链表长度   对象方法"""
        """cur游标，初始时是指向头节点， 用来移动遍历节点"""
        cur = self.__head
        if cur == None:
            count = 0
        else:
            count = 1
            while cur.next != None:
                count += 1
                cur = cur.next
        return count


    def travel(self):
        """遍历整个链表   对象方法"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")              # 去除换行符使用 end = " "
            cur = cur.next
        print("")


    def add(self, item):
        """链表头部添加元素  头插法 对象方法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):                              # item指具体的数据
        """链表尾部添加元素  尾插法 对象方法"""
        node = Node(item)                               # 先创建一个节点，用于保存item

        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        # if self.__head == None:                          # 判断是否为空链表
        #     self.__head = node
        cur = self.__head
        if self.is_empty():                                # 如果为空链表，则__head，即头指针是指向None的，而None是没有next，即没有链接域
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素   对象方法
        : param     pos 从0开始
        """
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length1() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            pre = self.__head                                 # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next                      # 先将新节点node的next指向插入位置的节点
            pre.next = node                             # 将插入位置的前一个节点的next指向新节点


    def remove(self, item):
        """删除节点     对象方法
        三种特殊情况需要考虑：一链表是否为空，二是否删除的是第一个元素，三是否删除的最后一个元素
        """
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先考虑特殊情况，链表第一个元素就等于要删除的元素
                if cur == self.__head:

                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next

                # 将删除位置前一个节点的next指向删除位置的后一个节点
                else:
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next


    def search(self, item):
        """查找节点是否存在    对象方法"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


# single_link = SingleLinkList()
# single_link.add()

if __name__ == "__main__":
    singlelist = SingleLinkList()
    print(singlelist.is_empty())          # True
    print(singlelist.length1())           # 0
    print(singlelist.length2())             # 0

    singlelist.append(1)
    print(singlelist.is_empty())           # False
    print(singlelist.length1())            # 1
    print(singlelist.length2())           # 1

    singlelist.append(2)
    singlelist.add(8)
    singlelist.insert(-1, 10)
    singlelist.travel()                     # 10 8 1 2
    singlelist.insert(0, 15)
    singlelist.travel()                    # 15 10 8 1 2
    singlelist.insert(4, 20)
    singlelist.travel()                    # 15 10 8 1 20 2
    singlelist.insert(9, 25)
    singlelist.travel()                   # 15 10 8 1 20 2 25
    singlelist.insert(7, 30)
    singlelist.travel()                   # 15 10 8 1 20 2 25 30
    singlelist.append(3)
    singlelist.append(4)
    singlelist.append(5)
    singlelist.travel()                  # 15 10 8 1 20 2 25 30 3 4 5

    print(singlelist.search(100))    # False
    print(singlelist.search(20))     # True

    singlelist.remove(5)
    singlelist.travel()
    singlelist.remove(15)
    singlelist.travel()
    singlelist.remove(1)
    singlelist.travel()