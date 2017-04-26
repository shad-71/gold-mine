from queue import *

def structure_test():
    Q = queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(7)
    Q.enqueue(8)
    Q.enqueue(9)
    Q.enqueue(11)
    Q.enqueue(12)
    Q.enqueue(22)
    Q.enqueue(32)

    print Q.front()
    print Q.rear()
    print Q.dequeue()
    print Q.dequeue()
    print Q.dequeue()
    print Q.front()

def Priority_Q_test():
    PQ = PriorityQueue()
    PQ.enqueue(31,1)
    PQ.enqueue(11,2)
    PQ.enqueue(91,4)
    PQ.enqueue(51,3)

    print PQ.front()
    print PQ.rear()

if __name__ == "__main__":
    # structure_test()
    Priority_Q_test()
