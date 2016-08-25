class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+=1
        while 10 in digits:
            index10=digits.index(10)
            if index10==0:
                digits[0]=0
                digits.insert(0,1)
                return digits
            digits[index10]=0
            digits[index10-1]+=1
        return digits