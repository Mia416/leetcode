'''
Created on Mar 25, 2019

@author: chenz
'''
class Solution(object):
    def rotate(self, nums, k):
        a = []
        i,j = 0,0
        for i in range(0,len(nums)-1):
            print(nums[i])
            print ((i+k) % len(nums))
            a.insert((i+k) % len(nums), nums[i])
            ##a[(i+k) % len(nums)] = nums[i]
        
        for j in range(0,len(nums)-1):
            nums[j] = a[j]

s1 =  Solution();
print (s1.rotate([1,2,3,4,5,6,7],3))