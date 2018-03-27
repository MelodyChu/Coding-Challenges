def is_anagram_of_palindrome(word):
    # first one and last one
    # spelled same forwards and backwards
    # racecar dad aba
    # one letter needs to appear at least twice
    word_dict = {}
    if len(word) == 1:
        return True

    elif len(word) > 1:
        for letter in word:
            if letter not in word_dict:
                word_dict[letter] = 1
            else: 
                word_dict[letter] += 1

    # if length is even; need multiples of 2 for every letter
    # if length is odd; need multiples of 2 for every letter but 1 letter can be odd 
    # {r: 2, a: 2, c: 2, e: 1}
    
    even_length_count = 0
    if len(word) % 2 == 0: # if length is even
        for value in word_dict.values():
            if value % 2 == 0:
                even_length_count += 1
    if even_length_count == word_dict.values():
        return True

    odd_length_count = 0
    other_count = 0
    if len(word) % 2 != 0:
        for value in word_dict.values():
            if value % 2 == 0:
                odd_length_count += 1
            else:
                other_count += 1

    if odd_length_count % 2 == 0 and other_count % 2 != 0:
        return True
                

