class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def check_subsequence(s, t, m, n):
            #Base case
            if n == 0 and m > 0:
                return False
            
            if m <= 0 and n >=0 :
                return True
            
            #Choice diagram 
            if s[m-1] == t[n-1]:
                return check_subsequence(s, t, m-1, n-1)
            else:
                return check_subsequence(s, t, m, n-1)
        
        return check_subsequence(s, t, len(s), len(t))
