class Node( object ):
      def __init__( self, _data = None, _next = None ):
        self.data = _data
        self.next_= _next


def main():
   node = Node(5)
   print(node.data)


if __name__ == "__main__":
    main()

