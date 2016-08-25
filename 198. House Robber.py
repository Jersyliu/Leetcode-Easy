class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        result=range(len(nums))
        result[0]=nums[0]
        result[1]=max(nums[0],nums[1])
        for i in range(2,len(result)):
            result[i]=max(result[i-2]+nums[i],result[i-1])
        return result[-1]