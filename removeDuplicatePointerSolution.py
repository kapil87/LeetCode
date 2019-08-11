class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_pointer = 0
        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer +=1
                nums[slow_pointer] = nums[fast_pointer]
        return slow_pointer+1
