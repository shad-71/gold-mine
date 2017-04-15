from stack import stack

def InfixToPostfix(exp):
    """Method for infix to postfix conversrion"""
    _stack = stack()
    precedence = {'+':1,'-':1,'*':2, '/':2, '^':3}
    for i in exp:
        if i.isalpha():
            print i
        elif i == '(':
            _stack.push(i)
        elif i == ')':
            while _stack.peek() != '(' and not _stack.isEmpty():
                print _stack.pop()
        else:
            #if precedence[i] < precedence[_stack.peek()]:
            while not _stack.isEmpty() and precedence[i] <= precedence[_stack.peek()]:
                print _stack.pop()
            _stack.push(i)
    
    while not _stack.isEmpty():
        print _stack.pop()

    




