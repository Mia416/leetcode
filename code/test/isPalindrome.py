'''
Created on Mar 20, 2019

@author: chenz
'''

import re

class Solution(object):
    def isPalindrome(self, s):
        
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]','', s).lower()
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return False
                break;
            else:
                j = j-1
                i = i+1
        return True        
        
        
s1 =  Solution();
if (s1.isPalindrome('A man, a plan, a canal: Panama')):
    print('True')
else:
     print('False')   
