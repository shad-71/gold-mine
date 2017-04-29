from queue import *

def maxinwindow(arr, k):
    dq = deque()
    for i in range(0, k):
        if not dq.isEmpty() and arr[i] > arr[dq.rear()]:
            dq.deleteBack()
        dq.insertBack(i)

    for i in range(k,len(arr)):
        print arr[dq.front()]
        while not dq.isEmpty() and dq.front <= i - k:
            dq.deleteFront()
        while not dq.isEmpty() and arr[i] >= arr[dq.rear()]:
            dq.deleteBack()
        dq.insertBack(i)
    print arr[dq.rear()]
    