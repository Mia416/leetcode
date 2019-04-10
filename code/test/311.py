'''
Created on Mar 11, 2019

@author: chenz
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m1 = m+n-1;
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m=m-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n=n-1
         
        nums1[0:n] = nums2[0:n]           





s1 =  Solution();
print (s1.merge([1,9]))