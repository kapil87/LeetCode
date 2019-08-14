class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_brackets = ['(', '{', '[']
        close_brackets = {')': '(', '}': '{', ']': '['}
        
        for bracket in s:
            
            if bracket in close_brackets.keys():
                if stack:
                    if stack[-1] != close_brackets[bracket]:
                        return False
                    else:
                        #Remove the 
                        stack.pop()
                else:#Implies we have close braces but stack is empty
                    return False
            else:
                stack.append(bracket)
        return not stack
                
