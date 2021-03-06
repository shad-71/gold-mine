from queue import *
from circularTour import circularTour
from slidingwindow import maxinwindow
from LargestMultiple import multipleof3


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
    PQ.enqueue(1, 1)  # handles same priority with FIFO
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


def circularTour_problem():
    oil = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print "start jouney from :", circularTour(distance, oil)
    oil = [6, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print "start jouney from :", circularTour(distance, oil)
    distance = [4, 6, 3]
    oil = [6, 3, 7]
    print "start jouney from :", circularTour(distance, oil)


def slidingwindow_problem():
    arr = [1, 2, 3, 1, 4, 5, 2]
    maxinwindow(arr, 3)


def largestmultiple_problem():
    arr = [7, 1, 9]
    multipleof3(arr)


if __name__ == "__main__":
    # structure_test()
    # Priority_Q_test()
    # deque_test()
    # circularTour_problem()
    # slidingwindow_problem()
    largestmultiple_problem()
