"""Ideas were taken from https://stackoverflow.com/questions/9625663/calculating-and-printing-the-nth-prime-number/9704912 and https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n"""
import math
def prime_row(n):
    if n <=6:
        cases = {1:[2],2:[3,5],3:[7,11,13],4:[17,19,23,29],5:[31,37,41,43,47],6:[53,59,61,67,71,73]}
        return cases[n]
    last_prime_place = int((n*(n+1))/2)
    upper_limit = int(last_prime_place * (math.log(last_prime_place) + math.log(math.log(last_prime_place))))
    primes_to_limit = prime_generator(upper_limit)
    primes_to_last_place = primes_to_limit[:last_prime_place]
    
    return primes_to_last_place[(last_prime_place - n):]
def prime_generator(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

for i in range(1,10):
    
    print(prime_row(i))
