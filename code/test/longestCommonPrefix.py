'''
Created on Feb 28, 2019

@author: chenz
'''



def longestCommonPrefix(strs):
    if (len(strs)==0):
        return ""
    if (len(strs)==1):
        return strs[0]
    temp=""
    step=strs[0]
    
    for i in range(0,len(step)):
        flag = True 
            
        temp1 = step[0:i]   
        
        for j in range(1,len(strs)):
            if (len(strs[j])>=len(temp1)):
                    if not (strs[j][0:len(temp1)])==(temp1):
                        flag = False
                        break;
                   
            else:
                flag = False
    if(flag):
        temp = step[0:i]
      
    result = temp;
    return result;
        

print(longestCommonPrefix(["flower","flow","flight"]))
    