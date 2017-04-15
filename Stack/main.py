from stack import stack
from InfixToPostfix import InfixToPostfix

def structure_test():
    _stack = stack()
    _stack.push(2)
    _stack.push(3)
    print _stack
    print _stack.peek()
    _stack.pop()
    print _stack
    _stack.pop()
    print ("not empty", "empty")[_stack.isEmpty()]

def i2p_test():
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    InfixToPostfix(exp)


if __name__ == "__main__":
    #structure_test()
    i2p_test()
    