'''ii
Created on Mar 29, 2019

@author: chenz
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
         
        re = set()    
        for i in range(0,len(nums)):             
           re.add(nums[i])
        
        if len(re)==len(nums):
            return False
        else:
            return True
    
s1 =  Solution();
print (s1.containsDuplicate([3,3]))        