class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def next_number(s):
            """
            type: string
            rtype: string
            """
            result = []
            i = 0
            while i < len(s):
                count = 1
                #Check two conditions:
                #1. are we at the end i+1 < len(s)
                #2. Two indices we are comparing are equal, 
                #3. If yes, we need to increase the counter and i, once we get the different number, append the counter and number
                while i+1 < len(s) and s[i] == s[i+1]:
                    count +=1
                    i  +=1
                result.append(str(count)+s[i])
                i +=1
            #So far result is a list, take all the string numbers and join them to form single string.
            return "".join(result)
        
        #Begining string will always be 1
        s = '1'
        if n == 1:
            return s
        #We know 1st number, so we need to compute the rest of the n-1 numbers
        for i in range(n-1):
            s = next_number(s)
        return s
