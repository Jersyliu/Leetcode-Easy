class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k==0 or k==len(nums):
            return
        if k>len(nums):
            k%=len(nums)
        re=self.reserve(nums)
        print re
        p=self.reserve(re[:k])+self.reserve(re[k:])
        print p
        for i in range(len(p)):
            nums[i]=p[i]
        return 
    
    def reserve(self,nums):
        i=0
        j=len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums
        
            