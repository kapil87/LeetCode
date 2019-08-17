class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        #Replace all spaces, comma, and colon with empty space
        for special_char in r" ,<.>/?;:'\"{[]}!@#$%^&*()-_=+`~":
            if special_char in s:
                s = s.replace(special_char, '')
        #Or we can take the ascii values and chek if they are in 97-122 range
        #print s
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
        
