'''
Created on Apr 3, 2019

@author: chenz
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        s.sort()
        t=list(t)
        t.sort()
        print(s)
        print(t)
        if s==t :
            return True
        else:
            return False
        
s1 =  Solution();
print (s1.isAnagram('anagram','nagaram'))    