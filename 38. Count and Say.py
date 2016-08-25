class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result='1'
        k=1
        while k<n:
            temp=""
            le=len(result)
            i=0
            while i<le:
                if i==(le-1) or result[i]!=result[i+1]:
                    temp+=("1"+str(result[i]))
                    i+=1
                else:
                    num=i+1
                    while result[num]==result[i]:
                        num+=1
                        if num==le:
                            break
                    temp+=str(num-i)+str(result[i])
                    i=num
            result=temp
            k+=1
        return result