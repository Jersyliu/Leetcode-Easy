# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=head
        curr=head
        if head==None or head.next==None:
            return head
        curr=curr.next
        while curr!=None:
            if curr.val==prev.val:
                curr=curr.next
            else:
                prev.next=curr
                prev=curr
                curr=curr.next
        prev.next=None        
        return head
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        while curr!=None and curr.next!=None:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head