from stack import stack

def structure_test():
    _stack = stack()
    _stack.push(2)
    _stack.push(3)
    print _stack
    _stack.pop()
    print _stack
    _stack.pop()
    print ("not empty", "empty")[_stack.isEmpty()]

if __name__ == "__main__":
    structure_test()
