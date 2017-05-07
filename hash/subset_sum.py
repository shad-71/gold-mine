# It is classic sum of 2 numbers problem in a given array
# whose sum matches given value S

# for solution of this problem we have to choose between 
# tradeoff of time or space

def subset_sum_check(arr, value):
    i = 0
    numbers = {}
    for item in arr:
        numbers[i] = item
        i += 1

    for item in arr:
        if value - item in numbers:
            print "numbers are ", item, "-", value - item


