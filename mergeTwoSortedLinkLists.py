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
        dummyHead = mergeList = ListNode(None)#Dummy Head
        while l1 and l2:
            if l1.val <= l2.val:
                mergeList.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                mergeList.next = l2
                l2 = l2.next
            mergeList = mergeList.next

        while l1:
            mergeList.next = l1
            l1 = l1.next
            mergeList = mergeList.next

        while l2:
            mergeList.next = l2
            l2 = l2.next
            mergeList = mergeList.next
        return dummyHead.next #As we had dummy head so we need to return 1st node.
            
