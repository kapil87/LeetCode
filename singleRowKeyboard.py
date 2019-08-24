class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        w_distance = keyboard.index(word[0])
        for i in range(1, len(word)):
            w_distance += abs(keyboard.index(word[i])-keyboard.index(word[i-1]))
        return w_distance
            
