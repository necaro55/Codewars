#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

#Examples
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !
def pig_it(text):
    text += " "
    word = False
    start = 0
    processed = ""
    for x in range(len(text)):
        
        if word:
            if text[x].isalpha():
                processed += text[x]
                continue
            else:
                               
                processed += text[start] + "ay" + text[x]
                word = False
                continue
        
        if text[x].isalpha() :
            start = x
            word = True
            
        else:
            processed += text[x]
            
    return processed[:-1]
