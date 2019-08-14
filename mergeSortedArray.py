class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        count = m +n -1
        m -= 1
        n -= 1
        while (m >=0 and n >=0):
            if nums1[m] > nums2[n]:
                nums1[count] = nums1[m]
                count -=1
                m -=1
            else:
                nums1[count] = nums2[n]
                count -=1
                n -=1
        #There is case when we are done with nums1 but there are values in nums2, so we need to copy all those
        while n >=0:
            nums1[count] = nums2[n]
            count -=1
            n -=1
            
