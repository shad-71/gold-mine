class Node(object):
      def __init__(self, _data = None, _next = None):
        self.data = _data
        self.next= _next

class LinkedList (object):
    def __init__( self ):
        head = Node(None)
    
    def push(self, key):
        node = Node(key)
        if self.head.data is None:
            head = node
        else:
            node.next = head
            head = node


