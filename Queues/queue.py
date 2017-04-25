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




