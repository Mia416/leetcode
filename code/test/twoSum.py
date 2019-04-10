'''
Created on Mar 21, 2019

@author: chenz
'''
from _ast import Num
class Solution(object):
    def twoSum(self, numbers, target):
        re=[]
        for i in range(0,len(numbers)):
            temp = numbers[i]
            print (numbers.index(target-temp))
            try:
                if numbers.index(target-temp)>0:            
            ##for j in range(i+1,len(numbers)):
                 ##if target == temp + numbers[j] :
                     re.append(i+1)
                     re.append(numbers.index(target-temp)+1)
                     return re  
            except:  
                 continue             
                            
    def twoSum1(self,numbers,target):
        re=[]
        i,j = 0,len(numbers)-1
        while(i<j):
            temp = numbers[i] + numbers[j]
            if temp==target:
                re.append(i+1)
                re.append(j+1)
                return re
            else:
                 if temp<target:
                     i=i+1
                 else:
                     j=j-1
        return None        
                
    
             
                


s1 =  Solution();
print (s1.twoSum([0,0,3,4],0))