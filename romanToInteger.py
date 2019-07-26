def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not s:
        return 0

    length = len(s)
    result = romanValues[s[-1]]

    for i in range(length-2, -1, -1):
        #print i, s[i], s[i+1], result
        if romanValues[s[i]] >= romanValues[s[i+1]]:
            result += romanValues[s[i]]
        else:
            result -=romanValues[s[i]]

    return result
        
