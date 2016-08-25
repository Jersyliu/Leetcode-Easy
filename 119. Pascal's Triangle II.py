class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        preRow=self.getRow(rowIndex-1)
        bacRow=[1]
        for i in range(1,(rowIndex//2)+1):
            bacRow.append(preRow[i-1]+preRow[i])
        if rowIndex%2==0:
            bacRow=bacRow+bacRow[(rowIndex//2)-1::-1]
        if rowIndex%2!=0:
            bacRow=bacRow+bacRow[(rowIndex//2)::-1]
        return bacRow

a=Solution()
print a.getRow(2)