#Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    
    if array1 == None or array2 == None:
        return False
    if len(array1) == 0 and len(array2) == 0:
        return True
    if len(array1) != len(array2):
        return False
    array3 = [i**0.5 for i in array2]
    array4 = [abs(i) for i in array1]
    array4.sort()    
    array3.sort()
    
    for i in range(0,len(array3)):
        if abs(array4[i]) != array3[i]:
            
            return False
    return True
