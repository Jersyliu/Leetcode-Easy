class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n/2!=0:
            count+=n%2
            n/=2
        if n==1:
            count+=1
        return count