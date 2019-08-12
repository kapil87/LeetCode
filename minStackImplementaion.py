class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #We store x and value per stack
        #Using this approach we don't need to update the min once we remove min element from stack.
        min_value = min(self.min, x)
        self.stack.append((x, min_value))
        self.min = min_value
            
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop(-1)
            if self.stack:
                self.min = self.stack[-1][1]
            else:
                self.min = float("inf")
            

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
