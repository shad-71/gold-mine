class Node(object):
    def __init__(self, _data=None, _next=None):
        self.data = _data
        self.next = _next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def set_data(self, new_data):
        self.data = new_data


class LinkedList(object):
    """LinkedList Implementation."""

    def __init__(self, head=None):
        self.head = head

    def BulkAdd(self, _head, *argv):
        self.head = Node(_head)
        for arg in argv:
            self.push(arg)

    def push(self, key):
        node = Node(key)
        node.set_next(self.head)
        self.head = node

    def __str__(self, direction=None):
        if direction == "reverse":
            output = ""
            self.print_reverse(self.head, output)
        else:
            temp = self.head
            output = ""
            while temp:
                output = output + str(temp.get_data()) + "->"
                temp = temp.get_next()
            return output[:-2]

    def push_sorted(self, key):
        node = Node(key)
        temp = self.head
        while temp.get_data() < node.get_data():
            current = temp
            temp = temp.get_next()

        _next = current.get_next()
        current.set_next(node)
        node.set_next(_next)

    def reverse_iterative(self):
        current = self.head
        next = None
        previous = None

        while current:
            next = current.get_next()
            current.set_next(previous)
            previous = current
            current = next

        self.head = previous

    def print_reverse(self, node, output):
        if node:
            self.print_reverse(node.get_next(), output)
            output = output + str(self.head.get_data()) + "->"
        else:
            return output

    def reverse(self, k, _next=None):
        if _next:
            current = _next
        else:
            current = self.head
        #_next = None
        previous = None
        count = k
        while current and  count > 0:
            _next = current.get_next()
            current.set_next(previous)
            previous = current
            current = _next
            count -= 1
        if _next:
            self.head.set_next(self.reverse(k, _next))

        return previous

    def breaker(self, ll):
        slow = ll.head
        if slow.get_next():
            fast = slow.get_next()

        while fast:
            fast = fast.get_next()
            if fast :
                slow = slow.get_next()
                fast = fast.get_next()

        middle = LinkedList()
        middle.head = slow.get_next()
        slow.set_next(None)

        return ll, middle  

    def Merge(self, start, middle):
        result = LinkedList()
        result = start
        merger = start.head
        while merger.get_next():
            merger = merger.get_next()
        merger.set_next(middle.head)
        return result

    def MergeSort(self, ll):
        _ll = ll
        if ll is None or ll.head.get_next() is None :
            return ll

        start, middle = self.breaker(_ll)
        start = self.MergeSort(start)
        middle = self.MergeSort(middle)
        return LinkedList_Util.SortedMerge(start, middle)



class LinkedList_Util(object):
    """LinkedList Util functions Implementation."""

    @staticmethod
    def SortedMerge(A, B):
        result = LinkedList()
        if A.head is None:
            return B
        elif B.head is None:
            return A
        if A.head.get_data() > B.head.get_data():
            result.push(B.head.get_data())
            B.head = B.head.get_next()
            result.head.set_next(LinkedList_Util.SortedMerge(A, B).head)
        else:
            result.push(A.head.get_data())
            A.head = A.head.get_next()
            result.head.set_next(LinkedList_Util.SortedMerge(A, B).head)

        return result
    
    


