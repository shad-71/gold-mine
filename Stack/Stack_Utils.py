from __future__ import print_function
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
    """Function to evaluate the postfix expression"""
    _stack = stack()
    for i in exp:
        if i.isdigit():
            _stack.push(i)
        else:
            y = _stack.pop()
            x = _stack.pop()
            _stack.push(str(eval(x + i + y)))
    print (_stack.peek())

def check_parenthesis(exp):
    """Check for paranthesis in a expression"""
    opening_parenthesis = "({["
    closing_parenthesis = ")}]"
    _stack = stack()
    for i in exp:
        if opening_parenthesis.find(i) > -1:
            _stack.push(i)
        if closing_parenthesis.find(i) > -1:
            if _stack.peek() == opening_parenthesis[closing_parenthesis.find(i)]:
                _stack.pop()
            else:
                return False
    if _stack.isEmpty():
        return True
    else:
        return False

def next_greater(array):
    """Finds next greater element for complete array"""
    _stack = stack()
    _stack.push(array[0])
    for i in array[1:]:
        if i > _stack.peek():
            _stack.push(i)
        else:
            _stack.push(_stack.peek())
        print (_stack.peek(), end = ' ')
    print ("-1")








