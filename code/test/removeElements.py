'''
Created on Mar 27, 2019

@author: chenz
'''
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val ==val:
            head = head.next
        if not head:
            return head
        temp = head
        while temp is not None:
            if temp.next is not None and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head       