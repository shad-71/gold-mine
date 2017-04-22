from Stack_Utils import *
from stack import stack

def TowerOfHanoi(disk_count):
    """Iterative Solution for Tower of Hanoi problem"""
    pole_source = stack()
    pole_destination = stack()
    pole_aux = stack()
    for i in range(0,disk_count - 1):
        pole_source.push(disk_count - i)
    moves = pow(2,disk_count) - 1
    if disk_count%2 == 0:
        MakeLegalMoves(moves,pole_source, pole_destination, pole_aux)
    else:
        MakeLegalMoves(moves, pole_source,pole_aux, pole_destination)
    
    while not pole_destination.isEmpty():
        print pole_destination.pop()


def MakeLegalMoves(count, stack_A, stack_B, stack_C):
    for i in range(1,count):
        if i%3 == 1:
            if stack_C.isEmpty():
                 if not stack_A.isEmpty():
                     stack_C.push(stack_A.pop())
            else:
                if stack_A.peek() < stack_C.peek():
                    stack_C.push(stack_A.pop())
                else:
                    stack_C.push(stack_A.pop())
        if i%3 == 2:
            if stack_B.isEmpty():
                 if not stack_A.isEmpty():
                     stack_B.push(stack_A.pop())
            else:
                if stack_A.peek() < stack_B.peek():
                    stack_B.push(stack_A.pop())
                else:
                    stack_A.push(stack_B.pop())
        if i%3 == 0:
            if stack_C.isEmpty():
                 if not stack_B.isEmpty():
                     stack_C.push(stack_B.pop())
            else:
                if stack_B.isEmpty():
                    stack_B.push(stack_C.pop())
                elif stack_B.peek() < stack_C.peek():
                    stack_C.push(stack_B.pop())
                else:
                    stack_B.push(stack_C.pop())
     
