from LinkedList import LinkedList
from LinkedList import LinkedList_Util

def test_1():
        ll = LinkedList(1, 2, 3, 4)
        _ll = LinkedList(1,2,3,4)
        result = LinkedList_Util.AddNumbers(ll, _ll)
        print result

def play():
    ll = LinkedList()
    ll.push(1)
    print ll

def main():
 
    ll = LinkedList(1, 2, 3, 4)
    print ll
    ll.push_sorted(8)
    print ll
    ll.head = ll.reverse(5)
    print ll
    _ll = LinkedList(1, 2, 3, 4, 5)
    #loop list
    _ll.head.next.next.next.next.set_next(_ll.head.get_next())
    _ll.DetectandRemoveLoop()
    print _ll
    ll_3 = LinkedList(4)
    ll_3 = LinkedList_Util.SortedMerge(ll, _ll)
    print ll
    ll_3 = ll_3.MergeSort(ll)
    print ll_3



if __name__ == "__main__":
    test_1()
    play()
