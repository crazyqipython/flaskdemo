#!/usr/bin/python

class Node():
    
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next #the next field

    def setData(self, newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext        #the  class of Node

class OrderedList():

    def __init__(self):
        self.head=None #initial the linked list

    def is_empty(self):
        return self.head==[]

    def add(self, item):
        current=self.head #initial the add position
        previous=None
        found=False
        while current !=None and not found:
            if current.getData > item:
                found=True
            else:
                current=current.getNext() #move to the next field
                previous=current   #mothed to find the add location

        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        
        else:
            temp.setNext(current)
            previous.setNext(temp) #add the item to the position,previous=temp is wrong because if do that the value of previous is missing
    
    def search(self,item):
        found=False
        current=self.head
        while current != None and not found:

            if current.getData()==item:
                found=True

            else:
                current=current.getNext()
        return found                        # the method of search
            
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                #current=current.getNext()
                #previous=current          #find the location of the item
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()

        else:
            previous.setNext(current.getNext()) #remove the item referentse to the next filed previous.setNext()

if __name__=='__main__':
    l=OrderedList()
    l.add(4)
    l.add(3)
    l.add(7)
    l.add(5)
    l.add(12)
    print l
    print l.search(7)
    print l.search(6)
    print "remove and search"
    print l.search(3)

    l.remove(3)
    print  l.search(3)
    print l.search(5)
    l.remove(5)
    print l.search(5)

