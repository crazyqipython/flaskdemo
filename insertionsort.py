#coding:utf-8
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]  #数值向前移动
            position = position - 1#指针向前移动
        a_list[position] = current_value


#def insertion_sort_binarysearch(a_list):
    #for index in range(1, len(a_list)):
        #current_value = a_list[index]
        #position = index
        #low=0
        #high=index-1
        #while low<=high:
            #mid=(low+high)/2
            #if a_list[mid]>current_value:
                #high=mid-1
            #else:
                #low=mid+1
        #while position > low:
            #a_list[position] = a_list[position - 1]
            #position = position -1
        #a_list[position] = current_value


a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
#insertion_sort_binarysearch(a_list)
#print(a_list)
