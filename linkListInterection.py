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
        if headA == None or headB == None:
            return None
        
        firstListHead = headA
        secondListHead = headB
        
        while firstListHead != secondListHead:
            firstListHead = headB if firstListHead == None else firstListHead.next
            secondListHead = headA if secondListHead == None else secondListHead.next
        
        return firstListHead
    
