# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left=1
        right=1
        
        if root==None:
            return 0
            
        if root.left==None:
            left=1
        else:
            left=1+self.maxDepth(root.left)
            
        if root.right==None:
            right=1
        else:
            right=1+self.maxDepth(root.right)
            
        return max(left,right)

            