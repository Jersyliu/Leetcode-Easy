class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            i=0
            result=''
            while True:
                flag=strs[0][i]
                for j in strs:
                    if j[i]!=flag:
                        break
                else:
                    result+=flag
                    i+=1
                    continue
                return result
        except:
            return result