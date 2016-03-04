#!/usr/bin/python
class stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def get_out(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items==[]
        print 'the list is empty.'

if __name__=="__main__":
    s=stack()
    print s.is_empty()
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(8.4)
    print(s.get_out())
