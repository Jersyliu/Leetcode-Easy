class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    if (prices[j]-prices[i])>result:
                        result=(prices[j]-prices[i])
        return result
        
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=0
        while len(prices)>1:
            maxP=max(prices)
            index=prices.index(maxP)
            if index==0:
                prices.remove(maxP)
                continue
            minP=min(prices[:index])
            if (maxP-minP)>result:
                result=maxP-minP
            prices.remove(maxP)
        return result
        
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        maxP=max(prices)
        minP=min(prices)
        indexmax=prices.index(maxP)
        indexmin=prices.index(minP)
        if indexmax>indexmin:
            return maxP-minP
            
        else:
            if indexmax==0:
                maxresult=0
            else:
                maxresult=maxP-min(prices[:indexmax])
            
            if indexmin==len(prices)-1:
                minresult=0
            else:
                minresult=max(prices[(indexmin+1):])-minP
            return max(maxresult,minresult,self.maxProfit(prices[(indexmax+1):indexmin]))
            
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        minP=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<minP:
                minP=prices[i]
            else:
                if (prices[i]-minP)>profit:
                    profit=(prices[i]-minP)
        return profit
        
a=Solution1()
print a.maxProfit([7,2,4,1])