# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        resultLeft=True
        resultRight=True
        
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        
        if p.val==q.val:
            
            if p.left!=None and q.left!=None:
                resultLeft=self.isSameTree(p.left,q.left)
            elif p.left==None and q.left==None:
                resultLeft=True
            else:
                return False
                
            if p.right!=None and q.right!=None:
                resultRight=self.isSameTree(p.right,q.right)
            elif p.right==None and q.right==None:
                resultRight=True
            else:
                return False
                
            return (resultLeft and resultRight)
            
        return False