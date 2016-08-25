# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None
        lenA,lenB=0,0
        currA,currB=headA,headB
        while currA!=None or currB!=None:
            if currA!=None:
                lenA+=1
                currA=currA.next
            if currB!=None:
                lenB+=1
                currB=currB.next
        if lenA<lenB:
            headA,headB=headB,headA
        for i in range(abs(lenA-lenB)):
            headA=headA.next
        result=None
        while headA!=None:
            if headA.val==headB.val:
                if result==None:
                    result=headA
            else:
                result=None
            headA=headA.next
            headB=headB.next
        return result
        
        