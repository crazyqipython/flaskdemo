#!/usr/bin/python
#coding=utf-8
def mergesort(a_list):
	if len(a_list)>1:
            
	    mid=len(a_list)//2
	    lefthalflist=a_list[:mid]
	    righthalflist=a_list[mid:]
	
	    mergesort(lefthalflist)          #如果函数调用放在if外面会出现错误
	    mergesort(righthalflist)

            i=0;
	    j=0;
	    k=0;
	    while i<len(lefthalflist) and j<len(righthalflist):
	        if lefthalflist[i]<righthalflist[j]:
                    a_list[k]=lefthalflist[i]
		    i=i+1
		    k=k+1
	        else:
		    a_list[k]=righthalflist[j]
                    j=j+1
		    k=k+1	
	    while i<len(lefthalflist):
		    a_list[k]=lefthalflist[i]
                    i=i+1
                    k=k+1

	    while j<len(righthalflist):
		    a_list[k]=righthalflist[j]
                    j=j+1
                    k=k+1

	print "sored:" ,a_list	

if __name__=="__main__":
	l=[54,26,93,17,77,31,44,55,20]
        print 'previous',l
	mergesort(l)
	print "the last print:" ,l 

