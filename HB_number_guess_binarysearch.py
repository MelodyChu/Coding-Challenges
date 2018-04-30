
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
num_list = []
for i in range(1,101):
    num_list.append(i)
print num_list

def binary_search(num_list, val, num_guesses=1): # val is the integer you're looking for
    """Using binary search, find val in range 1-100. Return # of guesses."""

    
    # assert 0 < val < 101, "Val must be between 1-100"


    #num_guesses = 0
    if len(num_list) == 1: # base case, since we cut list e/ time
        return num_guesses
    
    guess_pivot = int((len(num_list)-1)/2)  # find the midpoint index
    print "GUESS PIVOT IS" + str(guess_pivot)
    print "GUESS PIVOT NUMBER IS " + str(num_list[guess_pivot])

    if num_list[guess_pivot] == val:
        return num_guesses
    # first_half = num_list[:guess_pivot]
    # second_half = num_list[guess_pivot:len(num_list)]
    
    # if guess_pivot == val:
    #     return num_guesses + 1

    # while guess_pivot != val:

    if val < num_list[guess_pivot]:
        # num_list = first_half
        print num_list
        num_guesses += 1
        return binary_search(num_list[:guess_pivot], val, num_guesses) # first num up to guess pivot
    else: # if val > guess_pivot
        # num_list = second_half
        print num_list
        num_guesses += 1
        return binary_search(num_list[guess_pivot:len(num_list)], val, num_guesses)
    

print binary_search(num_list, 33)






    #return num_guesses


