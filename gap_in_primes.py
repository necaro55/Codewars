import math
def gap(g, m, n):
    def isPrime(h):
        if h == 1 or h == 3 or h == 5:
            return True
        if h % 2 == 0 or h % 3 == 0 or h % 5 == 0:
            return False
        for i in range(6, int(math.sqrt(h)) + 1):
            if h % i == 0:
                return False
        return True
        
    last_prime = 0   
    
    for x in range(m, n+1):     
        
        if isPrime(x):            
            if last_prime == 0:
                last_prime = x                
                continue
                
            if x - last_prime == g:                
                return [last_prime, x]
                
            last_prime = x
        
    return None
