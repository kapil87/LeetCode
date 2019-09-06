class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.data = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.map[val] = len(self.data)
            self.data.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            index = self.map[val]
            self.map[self.data[-1]] = index
            self.data[index] = self.data[-1]
            self.data.pop()
            del(self.map[val])
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.data) == 0:
            return 0
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
