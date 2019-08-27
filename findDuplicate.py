class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Find interection of two runners
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        #Find entrance to the cycle
        hare = nums[0]
        while hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return tortoise
