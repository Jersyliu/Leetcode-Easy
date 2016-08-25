class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<5:
            if n==4:
                return False
            return True
        la=[n-5,n-6,n-7]
        lb=[e%4 for e in la]
        if 0 in lb:
            return True
        return False
        
a=Solution()
k=[1,2,3,4,5,6,7,8,9,0,100]
print [a.canWinNim(i) for i in k] 