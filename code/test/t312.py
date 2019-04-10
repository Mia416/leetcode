'''
Created on Mar 12, 2019

@author: chenz
'''
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None and q is None):
            return True
        if (p is None or q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ismirror(root,root)
    
    def ismirror(self,root1,root2):
        if (root1 is None and root2 is None):
            return True
        if (root1 is None or root2 is None):
            return False
        if (root1.val == root2.val  and self.ismirror(root1.right,root2.left) and self.ismirror(root1.left,root2.right)):
            return True