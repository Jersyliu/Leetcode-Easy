import string
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result=''
        flagm=0
        k=0
        for i in xrange(len(str)):
            k=i
            if str[i]!=' ':
                if str[i] in '+-':
                    flagm=1
                    break
                if str[i] in string.digits:
                    break
                return 0
        if flagm==1:
            result+=str[k]
            k+=1
        for j in xrange(k,len(str)):
            if str[j] in string.digits:
                result+=str[j]
            if str[j] not in string.digits:
                break
        if result=='' or result=='-' or result=='+':
            return 0
        if int(result)>2147483647:
            return 2147483647
        if int(result)<-2147483648:
            return -2147483648
        return int(result)
                