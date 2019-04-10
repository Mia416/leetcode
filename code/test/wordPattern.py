'''
Created on Apr 9, 2019

@author: chenz
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")
        if len(pattern)!=len(str_list):
            return False
        dict={}
        for i in range(len(pattern)):
            if (pattern[i] not in dict):
                if str_list[i] not in dict.values():
                    dict[pattern[i]]=str_list[i]
                else:
                    return False
            elif (dict[pattern[i]]!=str_list[i]):
                 return False
        return True
                
        