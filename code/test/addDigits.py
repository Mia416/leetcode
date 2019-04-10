'''
Created on Apr 4, 2019

@author: chenz
'''
 
class Solution(object):
    def addDigits(self, num):
        if num<10:
            return num 
        else:
            sum  = 0
            for d in list(str(num)):
                sum = sum+int(d)
            return self.addDigits(sum)  

s1 =  Solution();
print(s1.addDigits(38))