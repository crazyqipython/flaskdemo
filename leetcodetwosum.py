#!/usr/bin/python
class solution():
    def twosum(self, nums, target):
        solu_result=[]
        lennum = len(nums)
        for i in range(lennum):
            if nums[i]+nums[i]==target:    #find same values
                solu_result.append([i,i]) 
            for j in range(i+1,lennum):
                if nums[i]+nums[j]==target: #find the diff indexs
                    solu_result.append([i,j]) 
        return solu_result

#the second solution,use dict 
class Solution():            #this method can't find all the possiable solution
    def twosum(self,nums,target):
        dict={}
        for i in range(len(nums)):
            if dict.get(target-nums[i],None)==None:
                dict[nums[i]]=i
            else:
                return (dict[target-nums[i]]+1, i+1)
if __name__=='__main__':
    ts=solution()
    list=[0,2,4,6,8,12,14]
    target=12
    print ts.twosum(list,target)

    print 'dict test'
    tsd=Solution()
    print tsd.twosum(list,target)
