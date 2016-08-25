# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        stack=[(root,root.val)]
        while stack:
            (node,sumUp)=stack.pop(0)
            if node.right==None and node.left==None:
                if sumUp==sum:
                    return True
                continue
            if node.right!=None:
                stack+=[(node.right,sumUp+node.right.val)]
            if node.left!=None:
                stack+=[(node.left,sumUp+node.left.val)]
        return False