from Stack_Utils import *
from stack import stack
from stock import *
from towerofhanoi import *
import timeit


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
    exp_i2p = "a+b*(c^d-e)^(f+g*h)-i"
    exp = "2+3*1-9"
    postfix_exp = InfixToPostfix(exp)
    print postfix_exp
    Eval_Postfix(postfix_exp)

def paranthesis_test():
    exp = "{()}[]"
    print ("paranthesis are not balanced", " paranthesis are balanced")[check_parenthesis(exp)]

def nge_test():
    ar = [4, 5, 2, 25]
    next_greater(ar)

def StockSpan_problem():
    prices = [10, 4, 5, 90, 120, 80, 90]
    StockSpan(prices)

def TowerOfHanoi_problem():
    TowerOfHanoi(100)


if __name__ == "__main__":
    #structure_test()
    #i2p_test()
    #paranthesis_test()
    #nge_test()
    #StockSpan_problem()
    TowerOfHanoi_problem()
    