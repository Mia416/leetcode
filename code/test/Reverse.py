'''
Created on Feb 26, 2019

@author: chenz
'''

def reverse(x):
    if x >= 0:
        x = int(str(x)[::-1])
        
    if x<0:
        x = -int(str(-x)[::-1])
    
    if (x>2147483647 ) or (x<-2147483647):
        return 0
    else:
        return x    
         
    

print(reverse(-321))