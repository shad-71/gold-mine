# Python program for implementation of stack
 
# import maxsize from sys module 
# Used to return -infinite when stack is empty
from sys import maxsize

class stack:
    """Stack structure """
    def __init__(self):
        self.stack = []

    def push(self, element):
        """for pushing a new elementin stack"""
        self.stack.append(element)

    def pop(self):
        """pop the element on top"""
        if not self.isEmpty():
            self.stack.pop()
        else:
            pass

    def isEmpty(self):
        """stack util for checking size"""
        return len(self.stack) == 0

    def __str__(self):
        output = ""
        for element in self.stack:
            output = output + str(element) + "->"
        return output[:-2]


