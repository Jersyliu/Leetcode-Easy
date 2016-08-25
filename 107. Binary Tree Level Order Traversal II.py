# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        result=[]
        leftList=self.levelOrderBottom(root.left)
        rightList=self.levelOrderBottom(root.right)
        
        if leftList==[] and rightList==[]:
            result.append([root.val])
            return result
        if leftList==[] and rightList!=[]:
            rightList.append([root.val])
            return rightList
        if leftList!=[] and rightList==[]:
            leftList.append([root.val])
            return leftList
            
        lenleftList=len(leftList)
        lenrightList=len(rightList)
        if lenleftList<=lenrightList:
            i=0
            while i<(lenrightList-lenleftList):
                result.append(rightList[i])
                i+=1
            j=0
            while j<lenleftList:
                result.append(leftList[j]+rightList[i+j])
                j+=1
        if lenleftList>lenrightList:
            i=0
            while i<(lenleftList-lenrightList):
                result.append(leftList[i])
                i+=1
            j=0
            while j<lenrightList:
                result.append(leftList[i+j]+rightList[j])
                j+=1
            
        result.append([root.val])
        return result
        
        
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        result=[]
        currLevel=[root]
        while len(currLevel)!=0:
            nextLevel=[]
            tempResult=[]
            for i in currLevel:
                tempResult.append(i.val)
                if i.left!=None:
                    nextLevel.append(i.left)
                if i.right!=None:
                    nextLevel.append(i.right)
                currLevel=nextLevel
            result.insert(0,tempResult)
        return result