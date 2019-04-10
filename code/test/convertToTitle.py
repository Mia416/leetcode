'''
Created on Mar 22, 2019

@author: chenz
'''
class Solution(object):
    def convertToTitle(self, n):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        res1 =""
        while n != 0:
            n -= 1 
            a = n % 26
            res += s[a]
            n = n // 26
        for i in range(len(res)-1,-1,-1):
                res1 =res1+res[i]
        return res1
    
    
   
        
s1 =  Solution();
print (s1.convertToTitle(26))