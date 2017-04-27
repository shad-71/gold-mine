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
    PQ.enqueue(31, 1)
    PQ.enqueue(11, 2)
    PQ.enqueue(91, 4)
    PQ.enqueue(51, 3)
    PQ.enqueue(10, 9)
    PQ.enqueue(1, 1) # handles same priority with FIFO
    PQ.enqueue(2, 5)
    PQ.enqueue(13, 6)


    print PQ.front()
    print PQ.rear()

    print PQ.dequeue()
    print PQ.dequeue()

    print PQ.front()
    print PQ.rear()

def deque_test():
    DQ = deque()
    DQ.insertBack(2)
    DQ.insertFront(1)

    print DQ.front()
    print DQ.rear()

    DQ.insertBack(3)
    DQ.insertFront(4)
    DQ.insertBack(5)
    DQ.insertFront(6)
    DQ.insertBack(7)
    DQ.insertFront(8)

    print DQ.front()
    print DQ.rear()

    DQ.deleteBack()
    print DQ.front()
    print DQ.rear()

    DQ.deleteFront()
    print DQ.front()
    print DQ.rear()

if __name__ == "__main__":
    # structure_test()
    # Priority_Q_test()
    deque_test()
