class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for word in strs:
            if tuple(sorted(word)) not in hashmap:
                hashmap[tuple(sorted(word))] = [word]
                
            else:
                hashmap[tuple(sorted(word))].append(word)
                
        return hashmap.values()
