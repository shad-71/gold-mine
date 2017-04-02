from LinkedList import LinkedList

def main():
    ll = LinkedList()
    ll.push(10)
    ll.push(7)
    ll.push(5)
    print ll
    ll.push_sorted(8)
    print ll
    ll.reverse()
    print ll
    ll.reverse()
    print ll

if __name__ == "__main__":
    main()

