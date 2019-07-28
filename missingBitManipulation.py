class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        missing =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
                =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
                =0∧0∧0∧0∧2
                =2	
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
            #Here each number and index
            #comes twice and missing comes only once
        return missing
