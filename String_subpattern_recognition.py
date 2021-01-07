#In this kata you need to build a function to return either true/True or false/False if a string can be seen as the repetition of a simpler/shorter subpattern or not.

#For example:

#has_subpattern("a") == False #no repeated pattern
#has_subpattern("aaaa") == True #created repeating "a"
#has_subpattern("abcd") == False #no repeated pattern
#has_subpattern("abababab") == True #created repeating "ab"
#has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern
#Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye on performances!).

import re
def has_subpattern(string):
    for x in range(1, len(string)):
        if string[0] == string[x]:
             
            if len(string) % len(string[0:x]) == 0:
                patternRepetition = re.findall(string[0:x], string)
                if (len(string) / len(string[0:x])) == len(patternRepetition):
                    return True
        if x > len(string)/2:
            return False
    return False

