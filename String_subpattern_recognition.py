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

