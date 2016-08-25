# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        while head.val==val:
            head=head.next
            if head==None:
                return None
        prev,curr=head,head.next
        while curr!=None:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head
            