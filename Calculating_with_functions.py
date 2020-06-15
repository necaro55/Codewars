def zero(n = False):
    if not n:
        return 0
    return n(0)
    
def one(n = False): 
    if not n:
        return 1
    return n(1)
def two(n = False): 
    if not n:
        return 2
    return n(2)
def three(n = False): 
    if not n:
        return 3
    return n(3)
def four(n = False): 
    if not n:
        return 4
    return n(4)
def five(n = False): 
    if not n:
        return 5
    return n(5)
def six(n = False): 
    if not n:
        return 6
    return n(6)
def seven(n = False): 
    if not n:
        return 7
    return n(7)
def eight(n = False): 
    if not n:
        return 8
    return n(8)
def nine(n = False): 
    if not n:
        return 9
    return n(9)

def plus(x): 
    def suma(n):
        return n + x
    return suma
def minus(x): 
    def menos(n):
        return n - x
    return menos
    
def times(x): 
    def por(n):
        return n * x
    return por
    
def divided_by(x): 
    def div(n):
        return n//x
    return div
