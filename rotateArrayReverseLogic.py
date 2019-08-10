class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            """
            Reverse elements in list from start to end
            """
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp 
                start +=1
                end -=1
            return nums
        k %= len(nums)
        #reverse full list
        reverse(nums, 0, len(nums)-1)
        #reverse 1st k elements in the list
        reverse(nums, 0, k-1)
        #reverse elements from k to the end of the list
        reverse(nums, k, len(nums)-1)
        #We are doing in-place modification, so check rtype of the rotate function
