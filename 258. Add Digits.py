class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        Hint:https://en.wikipedia.org/wiki/Digital_root
        """
        if num//10==0:
            return num
        addUp=0
        while True:
            addUp=addUp+(num%10)
            num=num//10
            if num==0:
                break
        return self.addDigits(addUp)
        
a=Solution()
print a.addDigits(34546)