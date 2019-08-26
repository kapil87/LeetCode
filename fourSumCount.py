class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum = {}
        for i in range(len(A)):
            for j in range(len(B)):
                sum[A[i] + B[j]] = sum.get(A[i]+B[j], 0) + 1
        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                res += sum.get(-(C[i]+D[j]), 0)
        return res
