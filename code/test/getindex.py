'''
Created on Feb 27, 2019

@author: chenz
'''
def getindex(nums,target):
    index=0    
    for i in range(0,len(nums)): 
        if nums[i]>=target :
            index=i
            break;
        else:
            index=index+1   
    
    return index;    
    

nums = [1,3,5,7]
print(getindex(nums,2))