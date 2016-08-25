# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        queue=[(root,1)]
        while queue:
            curr=queue.pop(0)
            if curr[0].left==None and curr[0].right==None:
                return curr[1]
            if curr[0].left!=None:
                queue+=[(curr[0].left,curr[1]+1)]
            if curr[0].right!=None:
                queue+=[(curr[0].right,curr[1]+1)]
        