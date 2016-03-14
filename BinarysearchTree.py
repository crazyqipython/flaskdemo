#!/usr/bin/python
#coding=utf-8
#search tree property:each of the leftsubtree less than the root,and each of the right tree larger than the root

#Treenode creat the node and judgement the node property like leftchild and rightchild

class TreeNode():
    
    def __init__(self,key, val, left=None, right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        self.parent=parent

    def isleftchild(self):
        return self.parent and self.parent.leftchild==self
    def isrightchild(self):
        return self.parent and self.parent.rightchild==self
    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild
    def isroot(self):
        return not self.parent
    def isleaf(self):
        return not (self.leftchild or self.rightchild)
    def hasanychild(self):
        return self.leftchild or self.rightchild
    def hasbothchild(self):
        return self.leftchild and self.rightchild

    def replaceNodeData(self,key,val,left,right):  #change the node property
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        if self.hasleftchild():
            self.leftchild.parent=self
        if self.hasrightchild():
            self.rightchild.parent=self

class BinarysearchTree():
    
    def __init__(self):
        self.root=None
        self.size=0
    def lengh(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    #the method put is to insert key and val to the tree ,and call the private method _put to find the right insert posithion
    def put(self, key, val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1
    def _put(self,key,val,currentnode):
        if key<currentnode.key:
            if currentnode.hasleftchild():
                self._put(key,val,currentnode.leftchild)#recursivly call the _put method
            else:
                currentnode.leftchild=TreeNode(key,val,parent=currentnode)
                #parent=currentnode is mean to reference each self
        else:
            if currentnode.hasrightchild():
                self._put(key,val,currentnode.rightchild)
            else:
                currentnode.rightchild=TreeNode(key,val,parent=currentnode) #之前写错了debuge出来的。
    def __setitem__(self,key,val):
        self.put(key,val)
    
    #the given the parameter of the key and get the value.get method is like the put method that is search from the root and recusivly call the _get method
    def get(self, key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentnode):
        if not currentnode:
            return None          #the tree havn't has the key 
        elif currentnode.key==key:
            return currentnode
        elif key<currentnode.key:
            return self._get(key,currentnode.leftchild) #recursive the leftsubtree 
        else:
            return self._get(key,currentnode.rightchild)

    def __getitem__(self,key):
        return self.get(key)

#the hardest part is delete the item.It will call two method.there are three cases need to discuss.the first case is that the item is a leaf node ,just del it;and sencond case is the item has one child:the left of right,del the item then move the child to the parent left or to the right;the third case is very complicated I will explain on the del method

    def delete(self,key):  #三种情况，一种情况只有root且相等　二只有root不相等　三不只有root:找到了，和没找到
        if self.size>1:
            nodetoremove=self._get(key,self.root) #call the _get method
            if nodetoremove:
                if nodetoremove.key==key:
                    self.remove(nodetoremove)#call remove method 
                    self.size=self.size-1
                else:
                    raise KeyError('error,key not in the tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=0
        else:
            raise KeyError('error,key not in the tree')
    
    def __delitem__(self,key):
        self.delete(key)

    def spliceout(self):  #用于第三种情况：当删除键有两个子树时，要求找到右子树的值，将该值移到删除键位置后，此函数将删除此值
        if self.isleaf():  #第一种情况是叶子节点
            if self.isleftchild():
                self.parent.leftchild=None
            else:                                         #successor是右结点，这种情况应该不存在吧？
                self.parent.rightchild=None
        elif self.hasanychild(): #因为successor分为三种，第一种右子树的最小值，第二种当前值是父结点的左结点，那么successor就是父亲结点；第三种当前删除结点是父结点的右结点，那么successor就是父结点的successor,这里用到递归。
            if self.hasleftchild():
                if self.isleftchild():
                    self.parent.leftchild=self.leftchild   #当是第二种情况的时候，那么就是将要删除的值（即delete)赋值给successor的父节点?
                else:
                    self.parent.rightchild=self.leftchild        
                self.leftchild.parent=self.parent
            else:
                if self.isleftchild():
                    self.parent.leftchild=self.rightchild
                else:
                    self.parent.rightchild=self.rightchild
                self.rightchild.parent=self.parent             #由于successor的第二三种情况，会不会存在双结点呢？
    
    def findsuccessor(self): #the third remove case will call the method
        succ=None
        if self.hasrightchild():#拥有右子树
            succ=self.rightchild.findmin() #call the findmin method

        else:
            if self.parent: #没有右子树，有父节点
                if self.isleftchild():
                    succ=self.parent
                else:
                    self.parent.rightchild=None
                    succ=self.parent.findsuccessor()
                    self.parent.rightchild=self #当没有右子树，且是右节点时，successor是父结点的successor
        return succ

    def finmin(self):
        current=self
        while current.hasleftchild():
            current=current.leftchild
        return current                 #最小值是左叶子结点

    def remove(self,currentnode):  #three 情况，第一种情况是叶子结点，第二种情况有一个子结点：分左子结点和右子结点；第三种情况，有两个子节点
        if currentnode.isleaf():
            if currentnode==currentnode.parent.leftchild:
                currentnode.parent.leftchild=None
            else:
                currentnode.parent.rightchild=None
        elif currentnode.hasbothchild():  #拥有两个子结点
            succ=currentnode.findsuccessor()#call findsuccessor method
            succ.spliceout()                #调用spliceout
            currentnode.key=succ.key
            currentnode.payload=succ.payload

        else: #有一个子结点
            if currentnode.hasleftchild():
                if currentnode.isleftchild():
                    currentnode.leftchild.parent=currentnode.parent
                    currentnode.parent.leftchild=currentnode.leftchild

                elif currentnode.isrightchild():
                    currentnode.leftchild.parent=currentnode.parent
                    currentnode.parent.rightchild=currentnode.leftchild
                else: #根结点
                    currentnode.replaceNodeData(currentnode.leftchild.key,
                                        currentnode.leftchild.payload,currentnode.leftchild,currentnode.leftchild.rightchild)

            else:#有右子结点
                if currentnode.isleftchild():
                    current.rightchild.parent=currentnode.parent
                    currentnode.parent.leftchild=currentnode.rightchild
                elif currentnode.isrightchild():
                    currentnode.rightchild.parent=currentnode.parent
                    currentnode.parent.rightchild=currentnode.rightchild
                else:
                    currentnode.replaceNodeData(currentnode.rightchild.key,currentnode.rightchild.payload,currentnode.rightchild.leftchild,currentnode.rightchild.rightchild)

if __name__=='__main__':
    b=BinarysearchTree()
    b[3]='red'
    b[4]='blue'
    b[6]='yellow'
    b[2]='at'
    print b[6]
    print b[2]
    print b[4]
    print b.lengh()
    b.delete(2)
    print b.lengh()
    print b[2]
