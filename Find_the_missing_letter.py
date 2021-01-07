#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

#['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

#["a","b","c","d","f"] -> "e"
#["O","Q","R","S"] -> "P"

def find_missing_letter(chars):
    missingLetter = ""
    counter = ord(chars[0])
    for i in chars:
        letterNumber = ord(i)
        if letterNumber != counter:
             missingLetter = chr(counter)
             break
        counter += 1
            

    return missingLetter
