# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return l1
        if l1==None and l2!=None:
            return l2
        if l2==None and l1!=None:
            return l1
        if l1.val<=l2.val:
            k=l1
            com=l2
        else:
            k=l2
            com=l1
        q=k
        while q.next!=None:
            if q.next.val>com.val:
                temp=q.next
                q.next=com
                com=temp
            q=q.next
        q.next=com
        return k
        