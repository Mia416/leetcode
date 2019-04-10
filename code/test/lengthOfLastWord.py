'''
Created on Feb 27, 2019

@author: chenz
'''
 
def lengthOfLastWord(s):
    x = s.strip().split(" ")    
    return len(x[-1])


print(lengthOfLastWord("Hello World"))