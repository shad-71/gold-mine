# This program was wrttien to implement
# A fast power evaluating function

def power(x, y):
    """Recusrive function to evaluate power in O(log n)"""
    if y == 0:
        return 1
    temp = power(x,y/2)
    if y%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

def pow(x, y):
    """Iterative function to evaluate power in O(log n)"""
    temp = 1
    while y > 0:
        if y & 1:
            temp = temp*x
        y = y>>1
        x = x*x 

    return temp



if __name__ == "__main__":
    print pow(2,10)
    print pow(2,11)
    print pow(2,12)



