# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        qu=[root]
        while any([i!=None for i in qu]):
            tempResult=[]
            nextqu=[]
            for i in qu:
                if i==None:
                    tempResult+=[None]
                    continue
                else:
                    tempResult+=[i.val]
                nextqu+=[i.left]
                nextqu+=[i.right]
            if tempResult[:len(tempResult)/2]!=tempResult[:(len(tempResult)/2-1):-1]:
                return False
            qu=nextqu
        return True
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue=[root,root]
        while queue:
            t1=queue.pop(0)
            t2=queue.pop(0)
            if t1==None and t2==None:
                continue
            if t1==None or t2==None:
                return False
            if t1.val!=t2.val:
                return False
            queue+=[t1.left]
            queue+=[t2.right]
            queue+=[t1.right]
            queue+=[t2.left]
        return True
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)
        
    
    def isMirror(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val!=root2.val:
            return False
        return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)
        
