# Python program for implementation of stack
 
# import maxsize from sys module 
# Used to return -infinite when stack is empty
from sys import maxsize

class stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self, element):
        self.stack.remove(element)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        output = ""
        for element in self.stack :
            output = output + str(element) + "->"        
        return output[:-2]


