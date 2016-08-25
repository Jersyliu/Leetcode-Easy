# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if abs(self.score(root.left)-self.score(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def score(self,root):
        if root==None:
            return 0
        return 1+max(self.score(root.left),self.score(root.right))