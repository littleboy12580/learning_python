class BinTree(object):                            #创建树的类
    def __init__(self,value):
        self._data = value
        self._left = None
        self._right = None

    def insert(self,value):                       #树的节点插入，左子树小于根节点，右子树大于根节点
        if self is None:
            self = BinTree(value)
        else:
            if value < self._data:                #左边迭代插入
                if self._left:
                    self._left.insert(value)
                else:
                    self._left = BinTree(value)
            else:
                if self._right:                   #右边迭代插入
                    self._right.insert(value)
                else:
                    self._right = BinTree(value)

    def pre_order(self):                          #前序遍历
        if self:
            print(self._data,end=' ')
        if self._left:
            self._left.pre_order()
        if self._right:
            self._right.pre_order()

    def in_order(self):                           #中序遍历
        if self._left:
            self._left.in_order()
        if self:
            print(self._data,end=' ')
        if self._right:
            self._right.in_order()

    def post_order(self):                         #后序遍历
        if self._left:
            self._left.post_order()
        if self._right:
            self._right.post_order()
        if self:
            print(self._data,end=' ')

    def find_min(self):                           #获取最小值
        if self._left:
            return self._left.find_min()
        else:
            return self

    def find_max(self):                           #获取最大值
        if self._right:
            return self._right.find_max()
        else:
            return self

    def find(self,value):                         #查找树中是否有该值
        if value == self._data:
            return self
        elif value < self._data and self._left:
            return self._left.find(value)
        elif value > self._data and self._right:
            return self._right.find(value)
        else:
            return None

    def del_value(self,value):                    #删除特定值节点
        if self.find(value):
            if value<self._data:
                self._left=self._left.del_value(value)    #左边迭代删除
                return self
            elif value>self._data:
                self._right=self._right.del_value(value)  #右边迭代删除
                return self
            elif self._left and self._right:              #如果左右子树都存在，找到右子树里最小的来代替被删除节点
                tmp=self._right.find_min()._data
                self._data=tmp
                self._right=self._right.del_value(tmp)
                return self
            else:
                if self._left:
                    return self._left
                else:
                    return self._right
        else:
            return self

#测试代码
tree = BinTree(7)
tree.insert(5)
tree.insert(3)
tree.insert(11)
tree.insert(16)
tree.insert(6)
tree.insert(21)
tree.insert(2)
tree.insert(13)
tree.insert(19)
tree.pre_order()
print("*****")
print(tree.find_min()._data)
print(tree.find_max()._data)
if tree.find(6):
    print("树里存在该数据")
else:
    print("树里没有该数据")
tree.del_value(6)
tree.pre_order()
print("*****")
if tree.find(6):
    print("树里存在该数据")
else:
    print("树里没有该数据")
