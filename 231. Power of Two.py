class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n%2==0:
            n/=2
        if n==1:
            return True
        else:
            return False