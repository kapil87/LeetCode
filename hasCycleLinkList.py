# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def hasCycleListSolution(head):
            nodeList = []
            while head:
                if head in nodeList:
                    return True
                nodeList.append(head)
                head = head.next
            return False
        
        def hasCycleTwoPointerSolution(head):
            """Two pointer solution"""
            if head == None or head.next == None:
                return False
            
            slow = head
            fast = head.next
            
            while slow !=fast:
                if fast == None or fast.next == None:
                    return False
                slow = slow.next
                fast = fast.next.next
            return True
        return hasCycleTwoPointerSolution(head)
