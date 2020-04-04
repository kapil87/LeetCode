class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        output = []
        
        decompress = lambda a, b: output.extend([b] * a)
        
        for i in range(0, len(nums), 2):
            decompress(nums[i], nums[i+1])
        
        return output
        
        
