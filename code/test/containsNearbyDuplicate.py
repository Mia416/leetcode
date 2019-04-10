'''
Created on Apr 1, 2019

@author: chenz
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        re = dict()    
        for i in range(len(nums)):           
           if nums[i] in re:
                dist = i - re[nums[i]]
                if dist<=k:
                    return True
                else:
                    re[nums[i]] = i 
           else:
              re[nums[i]] =i
               
        return False
s1 =  Solution();
print (s1.containsNearbyDuplicate([1,0,1,1],1))     