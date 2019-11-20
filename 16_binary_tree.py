#! /usr/bin/env python
# _*_coding:utf-8_*_
# project: Data_Structure_with_Algorithm_python
# Author: zcj
# @Time: 2019/11/20 11:15

# >>> bool([])
# False
# >>> bool([None])
# True
# >>>

# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
class Node(object):
    """构造树节点"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree(object):
    """按照广度优先(层次)遍历法构造一颗二叉树"""
    def __init__(self):
        self.root = None              # 根节点

    def add(self, item):
        """添加节点"""
        node = Node(item)

        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
            return
        # 使用队列来保存需要遍历、处理的数据
        queue = []
        queue.append(self.root)
        # queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            if current_node.lchild is None:
                current_node.lchild = node
                return
            else:
                queue.append(current_node.lchild)

            if current_node.rchild is None:
                current_node.rchild = node
                return
            else:
                queue.append(current_node.rchild)


    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return

        queue = []
        queue.append(self.root)
        # queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            # print("node: %s" % current_node.elem)
            print(current_node.elem, end = " ")
            if current_node.lchild is not None:
                queue.append(current_node.lchild)
            if current_node.rchild is not None:
                queue.append(current_node.rchild)

    def preorder(self, node):                    # 传入node是因为每次递归遍历的时候每个子树的根节点不一样，根节点在发生变化
        """先序遍历"， 根左右"""
        #遍历终止条件
        if node is None:
            return

        print(node.elem, end = " ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def midorder(self, node):
        """中序遍历, 左根右"""
        if node is None:
            return

        self.midorder(node.lchild)
        print(node.elem, end = " ")
        self.midorder(node.rchild)

    def lastorder(self, node):
        """后序遍历， 左右根"""
        if node is None:
            return

        self.lastorder(node.lchild)
        self.lastorder(node.rchild)
        print(node.elem, end = " ")

"""
前序，中序，后序三种遍历顺序中，只要任意两种中包含中序就可以确定出一颗树,比如：知道前序和中序，后序和中序。
但是如果给的是前序和中序则是无法确定出一颗树的
"""

if __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)

    t.breadth_travel()
    # print("\n")
    print(" ")
    t.preorder(t.root)
    # print("\n")
    print(" ")
    t.midorder(t.root)
    # print("\n")
    print(" ")
    t.lastorder(t.root)






