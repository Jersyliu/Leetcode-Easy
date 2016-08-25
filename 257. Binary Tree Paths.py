# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:
            return []
        stack=[(root,str(root.val))]
        result=[]
        while stack:
            curr=stack.pop()
            if curr[0].left==None and curr[0].right==None:
                result+=[curr[1]]
            if curr[0].right!=None:
                stack+=[(curr[0].right,curr[1]+"->"+str(curr[0].right.val))]
            if curr[0].left!=None:
                stack+=[(curr[0].left,curr[1]+"->"+str(curr[0].left.val))]
        return result