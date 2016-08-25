class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        li=str.split(' ')
        if len(pattern)!=len(li):
            return False
        dic={}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if li[i] in [dic[k] for k in dic]:
                    return False
                dic[pattern[i]]=li[i]
            else:
                if dic[pattern[i]]!=li[i]:
                    return False
        return True