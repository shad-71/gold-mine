class queue:
    """Queue implementation"""
    def __init__(self):
        """default constructor"""
        self.Q = []

    def enqueue(self, item):
        """for pushing element from rear"""
        self.Q.append(item)

    def dequeue(self):
        """Will return the poped elememt from the front"""
        if not self.isEmpty():
            return self.Q.pop(0)

    def isEmpty(self):
        """stack util for checking size"""
        return len(self.Q) == 0

    def front(self):
        """returns front element"""
        if not self.isEmpty():
            return self.Q[0]

    def rear(self):
        if not self.isEmpty():
            return self.Q[-1]

class PriorityQueue:
    """Priority Queue implementation"""
    def __init__(self):
        """default constructor"""
        self.Q = []
        self.P = []

    def enqueue(self, item, priority):
        index = -1
        if len(self.P) == 0:
            self.P.append(priority)
            self.Q.append(item)
            return
        for i in self.P:
            if priority < i:
                index = self.P.index(i)
                break

        if index != -1 and index != len(self.P):
            # _priority = self.P[index]
            # _item = self.Q[index]
            # self.P[index] = priority
            # self.Q[index] = item
            # index += 1
            while index < len(self.P):
                _priority = self.P[index]
                _item = self.Q[index]
                self.P[index] = priority
                self.Q[index] = item
                priority = _priority
                item = _item
                index += 1
            self.P.append(priority)
            self.Q.append(item)
        else:
            self.P.append(priority)
            self.Q.append(item)
    
    def isEmpty(self):
        """stack util for checking size"""
        return len(self.Q) == 0

    def front(self):
        """returns front element"""
        if not self.isEmpty():
            return self.Q[0]

    def rear(self):
        if not self.isEmpty():
            return self.Q[-1]

    def dequeue(self):
        """Will return the poped elememt from the front"""
        if not self.isEmpty():
            self.P.pop(0)
            return self.Q.pop(0)

class deque:
    """double ended queue implementation"""

    def __init__(self):
        """default constructor"""
        self.Q =[]
    
    def isEmpty(self):
        """stack util for checking size"""
        return len(self.Q) == 0
    
    def insertBack(self, item):
        self.Q.append(item)
    
    def deleteBack(self):
        if not self.isEmpty():
            self.Q.pop()               

    def insertFront(self):
        self.Q.insert(0)




        













