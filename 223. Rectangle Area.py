class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        result=0
        result+=((D-B)*(C-A)+(H-F)*(G-E))
        if (min(D,H)-max(B,F))>0 and (min(C,G)-max(A,E))>0:
            result-=(min(D,H)-max(B,F))*(min(C,G)-max(A,E))
        return result