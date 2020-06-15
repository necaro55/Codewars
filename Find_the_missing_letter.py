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
