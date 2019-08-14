class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        longestCommonPrefix = ""
        
        for idx, c in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if idx >= len(strs[i]) or strs[i][idx] !=c:
                    return longestCommonPrefix
                
            longestCommonPrefix += c
        return longestCommonPrefix
            
