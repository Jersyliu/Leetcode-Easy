class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        
        five=0
        two=0
        q=n
        while q!=0:
            five+=q//5
            q//=5
        q=n
        while q!=0:
            two+=q//2
            q//=2
        return min(two,five)
        
        
a=Solution()
print a.trailingZeroes(25)