class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        for j in t:
            if j not in dic:
                return False
            if dic[j]==0:
                return False
            dic[j]=dic[j]-1
        
        for k in dic:
            if dic[k]!=0:
                return False
        
        return True