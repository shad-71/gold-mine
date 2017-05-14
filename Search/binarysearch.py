def binarysearch(arr, x) :
    l = 0
    r = len(arr)
    while r - l >=0:
        mid = l + (r - l)/2 #help in overflow problem
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            r = mid
        else:
            l = mid

def floor(arr, x):
    l = -1
    r = len(arr) - 1
    while r - l > 1:
        mid = l + ( r - l)/2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid
    if arr[r] == x:
        return r
    else:
        return -1

def ciel(arr, x):
    l = 0
    r = len(arr)
    while r - l > 1:
        mid = l + ( r - l)/2
        if arr[mid] <= x:
            l = mid
        else:
            r = mid
    if arr[l] == x:
        return l
    else:
        return -1

def occurence_count(arr, x):
    return ciel(arr, x) - floor(arr, x) + 1
            