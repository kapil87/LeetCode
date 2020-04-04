class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        _product = 1
        _sum = 0
        
        for num in str(n):
            _product *=int(num)
            _sum += int(num)
        
        return _product - _sum
