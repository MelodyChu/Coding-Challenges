"""You can perform the following operation on some string, :

Capitalize zero or more of 's lowercase letters at some index i (i.e., make them uppercase).
Delete all of the remaining lowercase letters in .
Given  queries in the form of two strings,  and , determine if it's possible to make  equal to  by performing the above operation on . If  can be transformed into , print YES on a new line; otherwise, print NO.

Input Format

The first line contains a single integer, , denoting the number of queries. The  subsequent lines describe each query in the following format:

The first line of each query contains a single string, .
The second line of each query contains a single string, .
Constraints

String  consists only of uppercase and lowercase English letters.
String  consists only of uppercase English letters.
Output Format

For each query, print YES on a new line if it's possible to make string  equal to string  by performing the operation specified above; otherwise, print NO.

Sample Input

1
daBcd
ABC
Sample Output

YES
Explanation

image

We have  daBcd and  ABC. We perform the following operation:

Capitalize the letters a and c(the characters in green font) in  so that  dABCd.
Delete all the remaining lowercase letters (the characters in red font) in  so that  ABC."""

import sys

def abbreviation(a, b):
    
    # lower strings a & b
    # quick win - if len(b)>len(a) then No
    # see if b exists in string a; if not, then No
    # outside of substring b, there can be no other capitalized words
    # if capitalized words not in b, No
    # Complete this function
    
    orig_a = a
    orig_b = b
    lower_a = a.lower()
    lower_b = b.lower()
    
    if len(b) > len(a):
        return "No"
    
    if lower_b not in lower_a:
        return "No"
    else: # if lower_b is in a
        for i in orig_a:
            i
        

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        a = raw_input().strip()
        b = raw_input().strip()
        result = abbreviation(a, b)
        print result
