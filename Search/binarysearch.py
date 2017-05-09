def binarysearch(arr, x) :
    l = 0
    r = len(arr)
    while r - l >=0:
        mid = l + (r - l)/2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            r = mid
        else:
            l = mid
            