class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hash_map = [0]*26
        for c in tasks:
            hash_map[ord(c)-ord('A')] +=1
        hash_map.sort()
        times = 0
        while(hash_map[25]>0):
            i = 0
            while(i <= n):
                if hash_map[25] == 0:
                    break
                if i < 26 and hash_map[25-i] > 0:
                    hash_map[25-i] -=1
                    
                times +=1
                i +=1
            hash_map.sort()
        return times
        
