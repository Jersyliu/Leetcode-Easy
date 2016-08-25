import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=''
        if x<0:
            result+='-'
            x=-x
        if x==0:
            return 0
        while x%10==0:
            x//=10
        while x!=0:
            result+=str(x%10)
            x//=10
        if abs(int(result))>2**31:
            return 0
        return int(result)