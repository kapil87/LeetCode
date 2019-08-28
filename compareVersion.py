class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        max_len = max(len(v1_list), len(v2_list))
        
        for i in range(max_len):
            v1 = int(v1_list[i]) if i < len(v1_list) else 0
            v2 = int(v2_list[i]) if i < len(v2_list) else 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
