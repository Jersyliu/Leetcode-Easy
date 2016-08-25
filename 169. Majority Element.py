class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        for j in dic:
            if dic[j]>(len(nums)//2):
                return j