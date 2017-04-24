from queue import queue

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

    print Q.dequeue()
    print Q.dequeue()
    print Q.dequeue()
    

if __name__ == "__main__":
    structure_test()
