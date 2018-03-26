"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""
    for i in range(1, len(alist)):
        for j in range(0,i):
            if alist[i] < alist[j]:
                current_val = alist.pop(i)
                # current_index = i
                # switch_val = alist[j]
                switch_index = j
                alist.insert(j,current_val)
                #alist[i], alist[j] = alist[j], alist[i]
    return alist

#reference here: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
