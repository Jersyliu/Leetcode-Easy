class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.li+=[x]

    def pop(self):
        """
        :rtype: nothing
        """
        self.li.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.li[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.li)==0
        