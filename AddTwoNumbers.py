# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        numbers = []
        carry = 0
        while(l1 or l2):
            if l1 and l2:
                sum = l1.val + l2.val + carry
                val = sum %10
                carry = int(sum/10)
                temp = ListNode(val)
                l1 = l1.next
                l2 = l2.next
                numbers.append(temp)
            elif l1:
                sum = l1.val + carry
                val = sum % 10
                carry = int(sum/10)
                temp = ListNode(val)
                l1 = l1.next
                numbers.append(temp)
            elif l2:
                sum = l2.val + carry
                val = sum % 10
                carry = int(sum/10)
                temp = ListNode(val)
                l2 = l2.next
                numbers.append(temp)
        if carry:
            temp = ListNode(carry)
            numbers.append(temp)
        for i in range(0, len(numbers)-1):
            numbers[i].next = numbers[i+1]
        return numbers[0]