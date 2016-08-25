class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        for j in dic:
            if dic[j]>1:
                return True
        return False