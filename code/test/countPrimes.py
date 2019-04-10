'''
Created on Mar 28, 2019

@author: chenz
'''
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n<2):
            return 0
        count = 1
        i = 3
        for i in range(3,n):
            if self.isPrime(i)==True:
                count=count+1
        return count
            
    def isPrime(self,n):
        if n % 2 == 0 :
            return False
        i = 3
        
        while i*i<=n:       
            if n%i==0:
                return False
            else:
                i=i+1   
        return True
     
s1 =  Solution();
print (s1.countPrimes(10))                    