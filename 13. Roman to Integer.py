class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={"I":1,"X":10,"C":100,"M":1000,"V":5,"L":50,"D":500}
        if len(s)==1:
            return dic[s]
        i=0
        result=0
        while i<len(s)-1:
             if dic[s[i]]<dic[s[i+1]]:
                 result+=dic[s[i+1]]-dic[s[i]]
                 i+=2
             else:
                 result+=dic[s[i]]
                 i+=1
        if i==len(s):
            return result
        if i==len(s)-1:
            return result+dic[s[-1]]