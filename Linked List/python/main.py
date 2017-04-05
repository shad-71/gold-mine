from LinkedList import LinkedList
from LinkedList import LinkedList_Util


def main():
    ll = LinkedList()
    ll.push(10)
    ll.push(7)
    ll.push(5)
    print ll
    ll.push_sorted(8)
    print ll
    ll.head = ll.reverse(5)
    print ll
    _ll = LinkedList()
    _ll.push(6)
    _ll.push(2)
    _ll.push(1)
    print _ll
    ll_3 = LinkedList()
    ll_3 = LinkedList_Util.SortedMerge(ll, _ll)
    print ll
    ll_3 = ll_3.MergeSort(ll)
    print ll_3


if __name__ == "__main__":
    main()
