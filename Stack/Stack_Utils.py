from stack import stack

def InfixToPostfix(exp):
    """Method for infix to postfix conversrion"""
    _stack = stack()
    output = []
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':-1, ')':-1}
    for i in exp:
        if i.isalpha() or i.isdigit():
            output.append(i)
        elif i == '(':
            _stack.push(i)
        elif i == ')':
            while _stack.peek() != '(' and not _stack.isEmpty():
                output.append(_stack.pop())
            if not _stack.isEmpty():
                _stack.pop()
        else:
            while not _stack.isEmpty() and precedence[i] <= precedence[_stack.peek()]:
                output.append(_stack.pop())
            _stack.push(i)
    
    while not _stack.isEmpty():
        output.append(_stack.pop())
    
    return "".join(output)

def Eval_Postfix(exp):
    _stack = stack()
    for i in exp:
        if i.isdigit():
            _stack.push(i)
        else:
            y = _stack.pop()
            x = _stack.pop()
            _stack.push(str(eval(x + i + y)))
    print _stack.peek() 



    




