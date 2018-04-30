"""
# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: for amount=4 (4) and denominations=[1,2,3] (1, 2 and 3), 

# 1, 1, 1, 1
# 1, 1, 2
# 1, 3
# 2, 2

# function takes in amount and list of denominations
# is amount divisible by any denominations? If so those are legit combinations
# if not and denom is smaller, what's the remainder? is remainder divisible by any denomination
# 4 % 1 - divisible; 4/1 = 4 
# 4 % 2 - divisble; 4/2 = 2
# 4 % 3 - not divisble; remainder is 1; 1 divisible by 1

# check are denoms always lower than amount given? no 0's in denoms right?
"""

def find_combos(amount, denominations):
    total_combos = 0 # will increment up each time
    for denom in denominations:
        if amount % denom == 0:
            total_combos += 1
        elif amount % denom != 0 and denom < amount:
            remainder = amount % denom
            for num in denominations:
                if remainder % num == 0:
                    total_combos += 1

        

    return total_combos

print find_combos(4, [1,2,3])

