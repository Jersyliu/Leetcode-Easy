class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in [dic[k] for k in dic]:
                    return False
                dic[s[i]]=t[i]
            else:
                if t[i]!=dic[s[i]]:
                    return False
        return True