'''
Created on Mar 11, 2019

@author: chenz
'''

class Solution(object):
    def removedup(self, nums1):
        list = set(nums1)
        return list



s1 =  Solution()
s2 = s1.removedup(['ad','ad','gg'])
print(s2)