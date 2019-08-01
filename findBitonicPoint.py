def findBitonicPoint(A):
    """A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing
    type nums: List[int]
    rtype: int
    """
    def binarySearch(a, left, right):
        """This problem can be solved with modified binary search"""
        if left <=right:
            mid = (left+right)//2
            #base condition to check if mid is the bitonic point
            if a[mid-1] < a[mid] and a[mid] > a[mid+1]:
                return mid
            if a[mid] < a[mid+1]:
                #We go to the right subarray if middle point is part of increasing subarray
                return binarySearch(a, mid+1, right)
            else:
                #Else we are part of decreasing subarray so check in left subarray
                return binarySearch(a, left, mid-1)
        return -1
    
    left, right = 0, len(A)-1
    return binarySearch(A, left, right)
    
