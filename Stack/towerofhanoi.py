from Stack_Utils import *
from stack import stack

def TowerOfHanoi(disk_count):
    """Iterative Solution for Tower of Hanoi problem"""
    pole_source = stack()
    pole_destination = stack()
    pole_aux = stack()
    for i in range(0,disk_count):
        pole_source.push(disk_count - i)
    moves = pow(2,disk_count) 
    if disk_count%2 == 0:
        MakeLegalMoves(moves,pole_source, pole_destination, pole_aux)
    else:
        MakeLegalMoves(moves, pole_source,pole_aux, pole_destination)
    
    while not pole_destination.isEmpty():
        print pole_destination.pop()


def MakeLegalMoves(count, stack_A, stack_B, stack_C):
    #for i in xrange(1,count):
    i = 1
    while i < count:
        if i%3 == 1:
            MoveDisk(stack_C, stack_A)
        if i%3 == 2:
            MoveDisk(stack_B, stack_A)
        if i%3 == 0:
            MoveDisk(stack_C, stack_B)
        yield i
        i += 1

def MoveDisk(stack_X, stack_Y):
    if stack_X.isEmpty():
        if not stack_Y.isEmpty():
            stack_X.push(stack_Y.pop())
    else:
        if stack_Y.isEmpty():
            stack_Y.push(stack_X.pop())
        elif stack_Y.peek() < stack_X.peek():
            stack_X.push(stack_Y.pop())
        else:
            stack_Y.push(stack_X.pop())

