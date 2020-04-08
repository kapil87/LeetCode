class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i, j, res = 0, len(A) - 1, -1
        
        while i < j:
            if A[i] + A[j] < K:
                res = max(res, A[i] + A[j])
                i += 1
            else: j -= 1
        
        return res
