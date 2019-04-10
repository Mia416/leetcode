'''
Created on Mar 8, 2019

@author: chenz
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)-1,-1,-1):           
            if(digits[i])!=9:
                digits[i]=digits[i]+1;
                return digits
            
            else:
                digits[i] = 0;            
        
        return [1]+digits

    
s1 =  Solution();
print (s1.plusOne([1,9]))