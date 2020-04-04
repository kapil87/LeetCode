class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Find digits with even numbers
        """
        digits_with_even_numbers = 0
        even_digits = lambda num : 1 if len(str(num))%2==0 else 0
        for num in nums:
            digits_with_even_numbers += even_digits(num)
                
        
        return digits_with_even_numbers
        
