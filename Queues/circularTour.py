from queue import *

def circularTour(distance,oil):
    Q = queue()
    Q.enqueue(0)
    n = len(distance)
    _sum = 0 
    while len(Q) < n:
        index = Q.rear()
        _sum += oil[index] - distance[index]
        while _sum < 0 and not Q.isEmpty():
            Q.dequeue()
        if Q.isEmpty():
            _sum = 0
        Q.enqueue((index+1)%n)
    return Q.front()


