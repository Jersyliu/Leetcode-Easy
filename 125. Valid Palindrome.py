import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='':
            return True
        s=s.lower()
        guide=string.punctuation+' '
        print s
        i,j=0,len(s)-1
        while i<j:
            while s[i] in guide and i<j:
                i+=1
            while s[j] in guide and i<j:
                j-=1
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        