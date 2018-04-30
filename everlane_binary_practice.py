# Write a function that takes a numerical value and returns the number of 
# most continuous 1's in the binary representation of that number. Include 
# the return value for argument '2928018016900296589618184185' and your code here:

# get binary representation of number
# start a counter / number
# number % 2; look at remainder
# if remainder is odd, append 1; if even, append 0
# stop when number to divide < 2

def count_binary(num):
    binary_list = []

    num_divided = num
    while num_divided > 0:
        remainder = num_divided % 2 # get remainder of 0 or 1
        num_divided = int(num_divided/2) # update num_divided each time
        binary_list.append(remainder) # append to binary_list regardless of 0 or 1

    binary_list =  binary_list[::-1] # reverse the binary list

    one_counter_list = []
    one_counter = 0
    for number in binary_list:
        if number == 1:
            one_counter += 1
        else:
            one_counter_list.append(one_counter)
            one_counter = 0 # reset one_counter each time 0 is reached

    return max(one_counter_list)

count_binary(2928018016900296589618184185)

