def count(string):    
    letter_counts = {}
    for letter in string:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts
