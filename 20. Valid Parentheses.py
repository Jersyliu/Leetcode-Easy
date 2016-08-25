class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s:
            if i in '([{':
                stack+=[i]
            if i in ')]}':
                if len(stack)==0 or stack.pop()!=dic[i]:
                    return False
        if len(stack)>0:
            return False
        return True