"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    # create a set; length should be 26
    # make sure every character in set is an alphabetical letter
    sentence = sentence.lower()
    alpha_set = set()

    for char in sentence:
        if char.isalpha():
            alpha_set.add(char)

    return len(alpha_set) == 26


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
