class Node(object):
      def __init__(self, _data = None, _next = None):
        self.data = _data
        self.next= _next

class LinkedList (object):
    head = Node(None)
    def __init__( self ):
        head = None
    
    def push(self, key):
        node = Node(key)
        node.next = self.head
        head = node
    
    def __str__(self):
        temp = self.head
        output = ""
        while temp:
            output = str(temp.data) + "->"
            temp = temp.next
        return output






