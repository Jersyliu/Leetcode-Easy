class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result=n
        L=[result]
        while result!=1:
            temp=0
            while result!=0:
                temp+=(result%10)**2
                result//=10
            result=temp
            if result in L:
                return False
            else:
                L.append(result)
        return True
        
a=Solution()
print a.isHappy(19)