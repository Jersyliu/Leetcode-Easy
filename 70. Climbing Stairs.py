class Solution(object):
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
        
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        qLimit=n//2
        result=0
        q=range(qLimit+1)
        p=[(n-2*i) for i in q]
        pandq=[p[j]+q[j] for j in range(len(q))]
        for k in range(len(pandq)):
            result+=(self.fact(pandq[k])/(self.fact(p[k])*self.fact(q[k])))
        return result

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        cache = {}
        cache[1], cache[2] = 1, 2

        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

a=Solution()
print a.climbStairs(7)
        