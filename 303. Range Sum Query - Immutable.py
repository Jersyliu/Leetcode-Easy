class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sumlist=[0]
        for i in range(len(nums)):
            self.sumlist+=[self.sumlist[i]+nums[i]]
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumlist[j+1]-self.sumlist[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)



class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums==[]:
            self.sumlist=[]
        elif len(nums)==1:
            self.sumlist=[nums[0]]
        else:
            self.sumlist=[nums[0]]
            for i in range(1,len(nums)):
                self.sumlist+=[self.sumlist[i-1]+nums[i]]
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.sumlist==[]:
            return 0
        if i==0:
            return self.sumlist[j]
        return self.sumlist[j]-self.sumlist[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)