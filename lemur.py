"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"
    counter = 0
    if len(branches) <= 1:
        counter = 0
    elif 1 < len(branches) <= 3:
        counter = 1
    else:
        for i in range(0,len(branches)-2, 2): # i is index; we're checking every other
            if branches[i + 2] == 0:
                counter += 1
                i += 2
            elif branches[i + 1] == 0:
                counter += 1

    return counter


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"