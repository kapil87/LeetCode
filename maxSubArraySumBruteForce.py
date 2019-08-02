
def maxSumSubArray(A):
    """Find the max sum in subarray using brute-force method"""
    sub_arrays = []
    max_sum= 0
    for i in range(0, len(A)):
        sub_array = []
        for j in range(i+1, len(A)+1):
            sub_arrays.append(A[i:j])
            if max_sum < sum(A[i:j]):
                max_sum = sum(A[i:j])
        
    return max_sum
