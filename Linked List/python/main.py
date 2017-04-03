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
    #print(ll,"reverse")
    _ll = LinkedList()
    _ll.push(4)
    _ll.push(2)
    _ll.push(1)
    ll_3 = LinkedList()
    ll_3 = ll.SortedMerge(ll,_ll)
    
    
    

if __name__ == "__main__":
    main()

