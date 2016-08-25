# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None or n==0:
            return head
        t=head
        i=0
        while i<n:
            t=t.next
            i+=1
        if t==None:
            return head.next
        curr=head
        while True:
            i=0
            temp=curr
            while i<(n+1):
                temp=temp.next
                i+=1
            if temp==None:
                curr.next=curr.next.next
                return head
            curr=curr.next
            