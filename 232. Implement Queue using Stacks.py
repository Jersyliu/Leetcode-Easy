class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=[]
    
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        return
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack1.remove(self.stack1[0])

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[0]
            

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1)==0