
def find_even_index(arr):
    leftSide = 0
    rightSide = 0
    fIndex = -1
    counter = 0
    for x in arr:
        if counter == 0:
            leftSide = 0
            for y in arr[1:]:
                rightSide += y                   
        else:
            for y in arr[:counter]:
                leftSide += y
            for z in arr[counter + 1 :]:
                rightSide += z
        
        if compareSides(leftSide, rightSide):
            fIndex = counter
            break
        else:
            leftSide = 0
            rightSide = 0
            counter += 1
            continue
        
            
        
    return fIndex 
        
                
            
            
def compareSides(left, right):
    if left == right:
        return True 
    else:
        return False
