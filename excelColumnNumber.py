class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        columnNumber = 0
        alphabetToNumber = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26
        }
        columnNumber = alphabetToNumber[s[-1]]
        counter = 1
        reversedColumnString = s[::-1]
        for i in reversedColumnString[1:]:
            columnNumber += pow(26,counter)*alphabetToNumber[i]
            counter += 1
        return columnNumber
         
