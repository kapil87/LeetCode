class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def addOne(digits, index):
            #print 'Returning with index: %s, digits: %s'% (index, digits)
            if index == 0 and digits[index] < 9:
                digits[index] += 1
                return digits
            elif index == 0 and digits[index] == 9:
                digits[index] = 0
                #temp = [0]*(len(digits)+1)
                #temp[0] = 1
                digits.insert(0,1)
                #return temp
                return digits
            elif digits[index] == 9:
                digits[index] = 0
                return addOne(digits, index-1)
            else:
                digits[index] +=1
                return digits
                    
        return addOne(digits, len(digits)-1)
