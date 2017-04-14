from stack import stack

def main():
    _stack = stack()
    _stack.push(2)
    _stack.push(3)
    print _stack
    _stack.pop(2)
    print _stack
    _stack.pop(3)
    print ("not empty", "empty")[_stack.isEmpty()]

if __name__ == "__main__":
    main()
