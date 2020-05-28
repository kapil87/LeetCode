class Solution:
    def decodeString(self, s: str) -> str:
        """Decode string, standard stack and queue problem"""
        if not s:
            return ""
        stack, end = [], 0
        while end < len(s):
            if s[end].isdigit():
                num = 0
                while end < len(s) and s[end].isdigit():
                    num = num*10 + int(s[end])
                    end += 1
                stack.append(num)
            elif s[end] == '[':
                stack.append("[")
                end += 1
            elif s[end].isalpha():
                temp = []
                while end < len(s) and s[end].isalpha():
                    temp.append(s[end])
                    end +=1
                stack.append("".join(temp))
            elif s[end] == ']':
                x = deque()
                while stack[-1] != '[':
                    x.appendleft(stack[-1])
                    stack.pop()
                stack.pop()
                if stack and type(stack[-1]) is int:
                    temp_str = "".join(x) * stack[-1]
                    stack.pop()
                    stack.append(temp_str)
                end += 1
        return "".join(stack)
                
