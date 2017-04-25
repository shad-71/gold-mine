# This program was wrttien to implement
# A fast power evaluating function
import timeit


def power(x, y):
    """Recusrive function to evaluate power in O(log n)"""
    if y == 0:
        return 1
    temp = power(x,y/2)
    if y%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

def powerI(x, y):
    """Iterative function to evaluate power in O(log n)"""
    temp = 1
    while y > 0:
        if y & 1:
            temp = temp*x
        y = y>>1
        x = x*x 

    return temp



if __name__ == "__main__":
    start_time = timeit.default_timer()
    print powerI(10,100000)
    print(timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    print pow(10,100000)
    print(timeit.default_timer() - start_time)



