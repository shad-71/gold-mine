from Queue import Queue

# @param arr : list of integers
# @return a list of integers
def prevSmaller(arr):
    q = Queue()
    output = []
    q.put(-1)
    if len(arr) <= 1:
        output.append(-1)
        return output
    for i in arr:
        temp = q.get()
        if i < temp:
            output.append(-1)
            q.put(i)
            q.put(temp)
        else:
            output.append(temp)
            q.put(i)
    return output
arr = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print prevSmaller(arr)