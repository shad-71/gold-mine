# This program was wrttien to implement a fast power evaluating function

def power(x, y):
    """Recusrive function to evalute power in O(log n)"""
    if y == 0:
        return 1
    
    temp = power(x,y/2)
    if y%2 == 0:
        return temp*temp
    else:
        return x*temp*temp


if __name__ == "__main__":
    print power(2,10)

