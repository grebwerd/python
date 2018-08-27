# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        nextNode = head
        prevNode = None

        while nextNode is not None:
            nextNode = nextNode.next
            head.next = prevNode
            prevNode = head
            
            if nextNode is not None:
                head = nextNode
            else:
                return head