# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        k=head
        i=0
        while k!=None:
            k=k.next
            i+=1
        t=head
        for j in range(i//2-1):
            t=t.next
        if i%2==0:
            tempHead=t.next
        else:
            tempHead=t.next.next
        curr=tempHead
        prev=None
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        while head!=None and prev!=None:
            if head.val==prev.val:
                head=head.next
                prev=prev.next
            else:
                return False
        return True
            
            