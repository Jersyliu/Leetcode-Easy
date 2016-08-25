class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        one=version1.split('.')
        two=version2.split('.')
        leng=max(len(one),len(two))
        
        for i in xrange(leng):
            one+=[0]
            two+=[0]
            if int(one[i])>int(two[i]):
                return 1
            if int(one[i])<int(two[i]):
                return -1
            if int(one[i])==int(two[i]):
                continue
        
        return 0