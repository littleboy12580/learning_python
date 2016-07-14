class TreeNode:
    def __init__(self,data):
        self._data=data
        self._left=None
        self._right=None
class BinTree:
    def insert(root,data):
        if root is None:
            root=TreeNode(data)
        else:
            if data<root._data:
                root._left=insert(root._left,data)
            else:
                root._right=insert(root._right,data)
        return root

    def pre_order(root):
        if root is not None:
            print(root._data,end=' ')
            pre_order(root._left)
            pre_order(root._right)

    def is_exist(root,data):
        if root is None:
            return None
        if root._data == data:
            return 1
        if root._data < data:
            return is_exist(root._right,data)
        else:
            return is_exist(root._left,data)

    def find_min(root):
        if root._left:
            return find_min(root._left)
        else:
            return root._data

    def find_max(root):
        if root._right:
            return find_max(root._right)
        else:
            return root._data
    def find(root,value):
        if root is None:
            return None
        if value == root._data:
            return root
        elif value<root._data:
            return find(root._left,value)
        else:
            return find(root._right,value)


    def del_value(root,value):
        if find(root,value):
            if value<root._data:
                root._left=del_value(root._left,value)
                return root
            elif value>root._data:
                root._right=del_value(root._right,value)
                return root
            elif root._left and root._right:
                tmp=find_min(root._right)
                root._data=tmp
                root._right=del_value(root._right,value)
                return root
            else:
                if root._left:
                    return root._left
                else:
                    return root._right
        else:
            return root

#    if value<root._data:
#       return del_value(root._left,value)
#    elif value>root._data:
#       return del_value(root._right,value)
#    else:
#       if(root._left and root._right):
#
#           tmp=find_min(root._right)
#           root._data=tmp._data
#           root._right=del_value(root._right,value)
#       else:
#           if root._left is None:
#               root=root.right
#           elif root._right is None:
#               root=root.left
#   return root

