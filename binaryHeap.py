#! /usr/bin/python

class BinaryHeap():
    def __init__(self):
        self.heapList=[0]
        self.currentsize=0

    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                temp=self.heapList[i]
                self.heapList[i]=self.heapList[i//2]
                self.heapList[i//2]=temp
            i=i//2                                  #if child is less than parent then exchangs the two items .inter the precesuer until reach the rood node.

    def insert(self,k): 
        self.heapList.append(k) 
        self.currentsize=self.currentsize+1 
        self.percUp(self.currentsize)       #insert the item initial the list and listsize then call the percUp function to put the item in the right position 
    
    def minChild(self,i):   #find the lowerest children and return it 
        if 2*i+1>self.currentsize: # whether the child node is the leave node 
            return 2*i
        else:
            if self.heapList[2*i]<self.heapList[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def perDown(self,i):
        while (2*i)<=self.currentsize:
            
            mc=self.minChild(i) #call the function minChild
            if self.heapList[i]>self.heapList[mc]:
                self.heapList[mc],self.heapList[i]=self.heapList[i],self.heapList[mc]
                #tmp=self.heapList[i]
                #self.heapList[i]=self.heapList[mc]
                #self.heapList[mc]=tmp
            i=mc

    def delMin(self):   #delete the min item
        self.heapList[1]=self.heapList[self.currentsize]
        self.heapList.pop()
        self.currentsize=self.currentsize-1
        self.perDown(1)  #from the root to put the item down,call the function of the perDown

    def buildheap(self,list):   #build a heap for  a given list
        i=len(list)//2
        self.currentsize=len(list)
        self.heapList=[0]+list[:] #the previous rows is to inintial the heap
        while (i>0):
            self.perDown(i)    #call the function perDown.get the larger item to the child node 
            i=i-1
            
if __name__=='__main__':
    b=BinaryHeap()
    #b.insert(3)
    #b.insert(2)
    #b.insert(1) 
    #print b.heapList
    #print b.currentsize
    a_list=[9,6,5,2,3]
    print a_list
    b.buildheap(a_list)
    print b.heapList, b.currentsize
    b.insert(10)
    b.insert(7)
    print b.heapList
    b.delMin()
    print b.heapList
    print b.currentsize

