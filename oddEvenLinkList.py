# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        odd = head
        even = head.next
        evenHead = even
        
        while even !=None and even.next !=None:
            #change next pointer of odd to even.next
            odd.next = even.next
            #update odd
            odd = odd.next
            #Now add odd.next to even.next
            even.next = odd.next
            #Update even
            even = even.next
        #In the end update odd.next with the head of evenHead
        odd.next =evenHead
        return head
        
