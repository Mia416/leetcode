'''
Created on Mar 27, 2019

@author: chenz
'''
class Solution(object):
    def isHappy(self, n):
        temp = set()
        while n!=1:
            if n in temp:
                return False
            temp.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True
            
            