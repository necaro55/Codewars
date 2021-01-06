#This time we want to write calculations using functions and get the results. Let's have a look at some examples:

#seven(times(five())); // must return 35
#four(plus(nine())); // must return 13
#eight(minus(three())); // must return 5
#six(dividedBy(two())); // must return 3
#Requirements:

#There must be a function for each number from 0 ("zero") to 9 ("nine")
#There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
#Each calculation consist of exactly one operation and two numbers
#The most outer function represents the left operand, the most inner function represents the right operand
#Division should be integer division. For example, this should return 2, not 2.666666...:

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
