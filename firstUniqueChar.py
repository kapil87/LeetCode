class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {}
        for c in s:
            if c in hashMap:
                hashMap[c] +=1
            else:
                hashMap[c] = 1
        #print hashMap
        #Pythonic version for building above hash would be using collections.Counter(s)
        for idx, c in enumerate(s):
            #Check if any char in hashMap appears only once, very 1st time and return that index
            if hashMap[c] == 1:
                return idx
        return -1
