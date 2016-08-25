class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return []
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
            if nums[i] not in dic:
                dic[nums[i]]=i
        return []