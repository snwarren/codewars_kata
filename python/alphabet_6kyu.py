#Welcome.
#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    output = []
    for i in text:
        if i.isalpha() == True:
            output.append(str(ord(i.lower()) - 96))
    return " ".join(output)