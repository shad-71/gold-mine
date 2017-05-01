# program it to find the largest multiple of 3 from the given array
from queue import queue

def multipleof3(arr):
    sorted(arr)
    q1 = queue()
    q2 = queue()
    q0 = queue()
    _sum = 0
    for i in arr:
        if i%3 == 0:
            q0.enqueue(i)
        if i%3 == 1:
            q1.enqueue(i)
        if i%3 == 2:
            q2.enqueue(i)
        _sum += i
    if _sum%3 == 0:
        print arr[::-1]
    if _sum%3 == 1 :
        if not q1.isEmpty():
            q1.dequeue()
        else:
            if len(q2) >= 2:
                q2.dequeue()
                q2.dequeue()
            else:
                print "number not possible"
        printmuliple(q0, q1, q2)
    if _sum%3 == 2:
        if not q2.isEmpty():
            q2.dequeue()
        else:
            if len(q1) >= 2:
                q1.dequeue()
                q2.dequeue()
            else:
                print "number is not possible"
        printmuliple(q0, q1, q2)

def printmuliple(q0, q1, q2):
    num = []
    while not q0.isEmpty():
        num.append(q0.dequeue())
    while not q1.isEmpty():
        num.append(q1.dequeue())
    while not q2.isEmpty():
        num.append(q2.dequeue())
    
    print sorted(num, reverse=True)






