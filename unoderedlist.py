class Node():
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        #tep.next=temp.setNext(self.head)   #wrong!!! call methond return None
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found



    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current !=None and not found: #find the item
             
            if current.getData() == item: #there is a bug if the current isthe last one of the data .because the last one reference to None
                found = True
            else:
                previous = current
                current = current.getNext()

        if current !=None:

            if previous == None:              #delete the the first number
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:                                        # the item not exists
            print "The %s can't exist" %item

if __name__=='__main__':
    linkl=UnorderedList()
    linkl.add(8)
    linkl.add(9)
    linkl.add(10)
    linkl.add(3)
    print linkl.size()
    print linkl.search(9)
    print linkl.search(34)
    linkl.remove(10)
    print linkl.size()
    linkl.remove(12)
