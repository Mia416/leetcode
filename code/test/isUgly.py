'''
Created on Apr 4, 2019

@author: chenz
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1 :
            return False
        if num ==0:
            return True
        
        while num % 2 ==0:
            num = num /2 
        while num % 5 ==0:
            num = num /5
        while num % 3 ==0:
            num = num /3
        if num == 1:
            return True
        return False