from binarysearch import *
from nose.tools import assert_equal, assert_raises

def binarysearch_test():
    arr = [1, 2, 3, 4, 8, 9]
    print "checking binary search"
    assert_equal(binarysearch(arr, 4), 3)
    print "success"

def occurence_count_test():
    arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    print "occurence test"
    assert_equal(occurence_count(arr, 2), 4)
    assert_equal(occurence_count(arr, 1), 3)
    assert_equal(occurence_count(arr, 4), 4)
    print "success"

if __name__ == "__main__":
    # binarysearch_test()
    occurence_count_test()
