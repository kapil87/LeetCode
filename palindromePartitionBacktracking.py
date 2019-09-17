class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        slength = len(s)
        
        def backtrack(partition, index):
            if index == slength:
                res.append(partition)
                return 
            
            for i in range(index, slength+1):
                substring = s[index: i+1]
                if substring == substring[::-1]:
                    backtrack(partition+[substring], i+1)
        
        backtrack([], 0)
        return res
