#!/usr/bin/env python
# encoding: utf-8

class BinTreeNode(object):               #创建节点类
    def __init__(self,data=0):
        self._data = data
        self._left = None
        self._right = None

class BinTree(BinTreeNode):              #创建二叉树类
    def create_tree(self,root):          #二叉树的初始化生成
        temp = input("请输入节点值:")
        if temp is '#':
            root = None
        else:
            root._data = temp            #按照先根节点再左节点后右节点的顺序存储
            root._left = BinTreeNode()
            self.create_tree(root._left)
            root._right = BinTreeNode()
            self.create_tree(root._right)

    def pre_order(self,root):            #前序遍历
        if root is not None:
            print(root._data,end=' ')
            self.pre_order(root._left)
            self.pre_order(root._right)


    def in_order(self,root):             #中序遍历
        if root is not None:
            self.in_order(root._left)
            print(root._data,end=' ')
            self.in_order(root._right)


    def post_order(self,root):           #后序遍历
        if root is not None:
            self.in_order(root._left)
            self.in_order(root._right)
            print(root._data,end=' ')







