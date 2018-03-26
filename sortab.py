"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10, 100])
    [1, 2, 3, 5, 6, 7, 8, 10, 100]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    # compare indexes of both lists; use 2 indices
    # when one index is finished, use another 

    new_list = []

    if len(a) == 0 and len(b) == 0:
        return a
    # else:
    #     a_index = 0
    #     b_index = 0
    #     while len(a) > 0 and len(b) > 0:
    #         if a[a_index] > b[b_index]:
    #             new_list.append(b[b_index])
    #             b.pop(b_index)
    #         elif a[a_index] < b[b_index]:
    #             new_list.append(a[a_index])
    #             a.pop(a_index)
    #         else: # if both are equal
    #             new_list.append(b[b_index])
    #             b.pop(b_index)
    #             # b_index += 1
    #             new_list.append(a[a_index])
    #             a.pop(b_index)
    #             # a_index += 1

    # if len(b) == 0:
    #     new_list.extend(a)
    # if len(a) == 0:
    #     new_list.extend(b)

    else:
        a_index=0
        b_index=0
        while a_index < len(a) and b_index < len(b):
            if a[a_index] > b[b_index]:
                new_list.append(b[b_index])
                b_index += 1
            else:
                new_list.append(a[a_index])
                a_index += 1


    if a_index < len(a):
        new_list.extend(a[a_index:])
    else:
        new_list.extend(b[b_index:])

    

    return new_list





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
