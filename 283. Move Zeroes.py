class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        zeronum=0
        nozeronum=0
        while i<len(nums):
            if zeronum+nozeronum==len(nums):
                return
            if nums[i]==0:
                zeronum=zeronum+1
                nums.remove(0)
                nums.append(0)
            else:
                nozeronum=nozeronum+1
                i=i+1
        return
        
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """        
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)
        return

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        L=[]       
        for i in range(len(nums)):
            if nums[i]!=0:
                L.append(i)
        if len(nums)-len(L)>0:
            for i in range(len(nums)):
                if i<len(L):
                    nums[i]=nums[L[i]]
                else:
                    nums[i]=0
        return
                   

nums=[0,1,0,3,12]
a=Solution()
a.moveZeroes(nums)
print nums