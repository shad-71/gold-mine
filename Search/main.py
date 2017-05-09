from binarysearch import binarysearch
from nose.tools import assert_equal, assert_raises

def binarysearch_test():
    arr = [1, 2, 3, 4, 8, 9]
    print "checking binary search"
    assert_equal(binarysearch(arr, 4),3)
    print "success"


if __name__ == "__main__":
    #test_1()
    binarysearch_test()
