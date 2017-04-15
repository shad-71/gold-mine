from stack import stack

def InfixToPostfix(exp):
    """Method for infix to postfix conversrion"""
    _stack = stack()
    output = []
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':-1, ')':-1}
    for i in exp:
        if i.isalpha():
            output.append(i)
        elif i == '(':
            _stack.push(i)
        elif i == ')':
            while _stack.peek() != '(' and not _stack.isEmpty():
                output.append(_stack.pop())
        else:
            while not _stack.isEmpty() and precedence[i] <= precedence[_stack.peek()]:
                output.append(_stack.pop())
            _stack.push(i)
    
    while not _stack.isEmpty():
        output.append(_stack.pop())
    
    print "".join(output)


    




