#!/usr/bin/python

class BinaryTree():
    def __init__(self, rootobj):
        self.key=rootobj
        self.leftchild=None
        self.rightchild=None

    def insertLeftChild(self, obj):
        if self.leftchild==None:
            self.leftchild=BinaryTree(obj)
        else:
            temp = BinaryTree(obj)
            temp.leftchild=self.leftchild
            self.child=temp                 #insert the subtree to the leftchild
    
    def insertRightChild(self, obj):
        if self.rightchild==None:
            self.rightchild=BinaryTree(obj)

        else:
            temp=BinaryTree(obj)
            temp.rightchild=self.rightchild
            self.rightchild=temp             #insert the right child

    def getRightchild(self):
        return self.rightchild #get the right subtree

    def getLeftchild(self):
        return self.leftchild  #get the left subtree

    def setRootval(self, obj):
        self.key=obj           #reset the tree value

    def getRootval(self):
        return self.key        #get the tree value


if __name__=='__main__':
    b=BinaryTree('a')
    print b.getLeftchild()
    b.insertLeftChild('b')
    b.insertRightChild('c')
    print b.getLeftchild()
    b.getLeftchild().setRootval('hello')
    print b.getLeftchild().getRootval()
    print b.getRightchild()
    b.getRightchild().setRootval('world')
    print b.getRightchild().getRootval()

