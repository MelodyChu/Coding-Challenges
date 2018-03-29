# Given a list of integers, find the highest product 
# you can get from three of the integers.

# Pseudo: figure out what the maximum 3 products are, and multiple them
# consider sorting first, and taking the last 3
# make sure only integers, can also have negative numbers; list always contains 3 things

def find_highest_product(alist):
    # first sort the list
    # if negative numbers; can only have 2 negative numbers; # check product of 2 lowest numbers; see
    alist.sort()
    if alist[0] < 0 and alist[1] < 0 and abs(alist[0]) > alist[len(alist)-1] and abs(alist[1] > alist[len(alist)-2]): # if lowest #'s are both negative
        print abs(alist[0])
        print alist[len(alist)-1]
        print abs(alist[1])
        print alist[len(alist)-2]
        return result
    else:
        product = alist[-1] * alist[-2] * alist[-3]
        return product

print find_highest_product([-1000, -199,0,1,999,1000])
