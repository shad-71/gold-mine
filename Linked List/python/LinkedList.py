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

    def __init__(self, _head=None, *argv):
        if _head:
            self.head = Node(_head)
        else:
            self.head = None    
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
        while temp and temp.get_data() < node.get_data():
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

    def DetectandRemoveLoop(self):
        slow = self.head
        fast = slow.get_next()
        while fast.get_data() != slow.get_data():
            fast = fast.get_next()
            if fast:
                slow = slow.get_next()
                fast = fast.get_next()
        slow = self.head
        while fast.get_data() != slow.get_data():
            fast = fast.get_next()
            if fast:
                loopNode = fast
                slow = slow.get_next()
                fast = fast.get_next()
        #culprit node is set none to break the loop       
        loopNode.set_next(None)

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.get_next()
        return length

    def countNine(self):
        nine = 0
        if self.head.get_next():
            temp = self.head
            list = LinkedList()
            list.head = temp
            list.head = list.head.get_next()
            nine = list.countNine()

        if self.head.get_data() == 9:
            if self.head.get_next():
                temp = self.head.get_next()
                if temp.get_data() == 9:
                    nine += 1
            else:
                nine += 1
        return nine

    def AddOne(self):
        length = len(self)
        list = self
        count = list.countNine()
        if count > 0 :
            if length == count:
                node = LinkedList()
                node.head = self.head
                node.makeZeros()
                self.push(1)
            else :    
                node = self.K_nodeFromLast(count,length)
                node.head.data += 1
                node.head = node.head.get_next() 
                node.makeZeros()
        else:
            self.AddOneToLast()
    
    def makeZeros(self):
        while self.head:
            self.head.set_data(0)
            self.head = self.head.get_next()
    
    def K_nodeFromLast(self, count, length):
        k = length - count - 1
        list = LinkedList()
        list.head = self.head
        while k > 0:
            list.head = list.head.get_next()
            k -= 1
        
        return list
    
    def AddOneToLast(self):
        list = LinkedList()
        list.head = self.head
        while list.head.get_next():
            list.head = list.head.get_next()
        
        list.head.data += 1


            


        

        




            






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

    @staticmethod
    def Add(A, B):
        result = LinkedList()
        carry = 0
        if len(A) > len(B):
            loop = len(A) - len(B)
            while loop:
                result.push(A.head.get_data())
                A.head = A.head.get_next()
                loop += 1          
            result.head.set_next(LinkedList_Util.Add(A, B).head)
            if carry:
                LinkedList_Util.Add(result, LinkedList(1))

        elif len(A) < len(B):
             loop = len(B) - len(A)
             while loop:
                result.push(B.head.get_data())
                A.head = B.head.get_next()
                loop += 1
             result.head.set_next(LinkedList_Util.Add(A, B).head)
             if carry:
                LinkedList_Util.Add(result, LinkedList(1))
        else :
            if A.head.get_next():
                A.head = A.head.get_next()
                B.head = B.head.get_next()
                result.head.set_next(LinkedList_Util.Add(A, B).head)
            else:
                temp = A.head.get_data() + B.head.get_data()
                if temp > 9:
                    if carry > 0:
                        result.push((temp%10)+1)
                        carry = 1
                    else:
                        result.push(temp%10)
                        carry = 1
                else:
                    if carry > 0:
                        if temp + carry > 9:
                            result.push((temp%10)+1)
                            carry = 1
                        else:
                            result.push(temp+1)
                            carry = 0
                    else:
                        result.push(temp)
                        carry = 0
                
        return result

    @staticmethod
    def AddNumbers( A, B):
        result = LinkedList()
        carry = 0
        if not B :
            return A
        
        if not A :
            return B

        if len(A) < len(B):
            while A:
                temp = A.head.get_data() + B.head.get_data() + carry
                if temp > 9:
                    result.push(temp%10)
                    carry = 1
                else :
                    result.push(temp)    
                    carry = 0
                A.head = A.head.get_next()
                B.head = B.head.get_next()
            while B:
                temp = B.head.get_data() + carry
                if temp > 9:
                    result.push(temp%10)
                    carry = 1
                else :
                    result.push(temp)
                    carry = 0
                B.head = B.head.get_next()
        else :
            while B:
                temp = A.head.get_data() + B.head.get_data() + carry
                if temp > 9:
                    result.push(temp%10)
                    carry = 1
                else :
                    result.push(temp)    
                    carry = 0
                A.head = A.head.get_next()
                B.head = B.head.get_next()
            while A:
                temp = A.head.get_data() + carry
                if temp > 9:
                    result.push(temp%10)
                    carry = 1
                else :
                    result.push(temp)
                    carry = 0
                A.head = A.head.get_next() 
        
        return result





