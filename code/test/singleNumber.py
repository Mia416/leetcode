'''
Created on Mar 20, 2019

@author: chenz
'''
class Solution(object):
    def singleNumber(self, nums):
        re = {}
        for i in range(0,len(nums)):
            if nums[i] in re:                
                del re[nums[i]]
            else:
                re[nums[i]]=i
        
        for j in re.keys():
            return j
        
s1 =  Solution();
print (s1.singleNumber([2,2,1]))