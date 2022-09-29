def anagrams(word, words):
    first_item = sorted(word)
    matches = []
    for each in words:
        second_item = sorted(each)
        if second_item == first_item:
            matches.append(each)
        
    return matches      
