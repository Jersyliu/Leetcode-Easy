class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li=s.split(' ')
        n=1
        while li[-n]=='' and n<len(s):
            n+=1
        return len(li[-n])