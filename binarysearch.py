#!/usr/bin/python
def findnumber(a_list, item):
    found=False
    first=0
    last=len(a_list)-1
    while not found:
        midpoint=(first+last)//2
        if item == a_list[midpoint]:
            found=True
            print 'the item is at %s' %midpoint
            return midpoint

        else:
            if item>a_list[midpoint]:
                first = midpoint +1

            else:
                last=midpoint - 1

a_list = [13, 15, 18, 19,25,28,39,40,50,56]
item=56
print findnumber(a_list,item)

