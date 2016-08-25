class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        result=[]
        for i in nums1:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        for j in nums2:
            if (j in dic) and dic[j]>0:
                result.append(j)
                dic[j]=dic[j]-1
        return result