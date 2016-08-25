# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        min=1
        max=n
        while min<max:
            mid=(min+max)//2
            if isBadVersion(mid)==True:
                max=mid
                continue
            else:
                min=mid+1
                continue
        return max