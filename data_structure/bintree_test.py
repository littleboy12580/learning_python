#!/usr/bin/env python
# encoding: utf-8

import my_bintree

node = my_bintree.BinTreeNode()
tree = my_bintree.BinTree()
tree.create_tree(node)
tree.pre_order(node)
tree.in_order(node)
tree.post_order(node)
