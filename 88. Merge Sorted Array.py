class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return 
        new=[]
        i,j=0,0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                new+=[nums1[i]]
                i+=1
            else:
                new+=[nums2[j]]
                j+=1
        if j<n:
            new+=nums2[j:n]
        if i<m:
            new+=nums1[i:m]
        for k in range(len(new)):
            nums1[k]=new[k]
        return
        