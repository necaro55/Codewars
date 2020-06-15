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
