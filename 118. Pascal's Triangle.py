class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        preresult=self.generate(numRows-1)
        preRow=preresult[-1]
        nowRow=[1]
        for i in range(1,(numRows//2+1)):
            nowRow.append(preRow[i-1]+preRow[i])
        print nowRow
        if numRows%2==0:
            nowRow=nowRow+nowRow[(numRows//2-2)::-1]
        if numRows%2!=0:
            nowRow=nowRow+nowRow[(numRows//2-1)::-1]
        print nowRow
        preresult.append(nowRow)
        return preresult
        
a=Solution()
print a.generate(4)
