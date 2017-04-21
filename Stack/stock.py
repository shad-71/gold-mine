from Stack_Utils import *
from stack import stack

def StockSpan(prices):
    """Stcok sapn problem"""
    _stack = stack()
    _stack.push(0)
    length = len(prices)
    span = 1
    print "Span for stock at day 1 is {0} ".format(span)

    for i in range(1, length):
        if not _stack.isEmpty() and prices[_stack.peek()] <= prices[i]:
            _stack.pop()
        if _stack.isEmpty():
            span = i + 1
        else:
            span = i - _stack.peek()
        print "Span for stock at day {0} is {1} ".format(i+1,span)
        _stack.push(i)


