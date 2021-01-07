#There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

#A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

#As a simplification, you may assume that no letter occurs more than once in the secret string.

#You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

def recoverSecret(triplets):
    flag = True
    x = []
    for i in triplets:
        x += i
    code = list(set(x))
    while flag:
        flag = False
        for i in triplets:
            if code.index(i[2]) < code.index(i[0]):
                code = swap(i[2], i[0], code)
                flag = True
            if code.index(i[2]) < code.index(i[1]):
                code = swap(i[2], i[1], code)
                flag = True
            if code.index(i[1]) < code.index(i[0]):
                code = swap(i[1], i[0], code)
                flag = True
    return "".join(code)

def swap(a, b, source):
    index_a = source.index(a)
    index_b = source.index(b)
    source[index_a] = b
    source[index_b] = a
    return source
