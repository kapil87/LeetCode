class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        def isPrime(n):
            """Check if number is prime"""
            if n <= 1:
                return False
            
            i = 2
            while i*i <= n:
                if n %i == 0:
                    return False
                i +=1
            return True
        
        count = 0
        for i in range(1, n):
            if isPrime(i):
                count +=1
        return count
        '''
        
        isPrime = [True]*n #We have already set all of them as True
        i = 2
        while i*i < n:
            if not isPrime[i]:
                continue
            j = i*i
            while j < n:
                isPrime[j] = False
                j +=i
            i +=1
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count +=1
        
        return count
        

            
