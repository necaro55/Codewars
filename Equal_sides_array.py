#You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

#For example:

#Let's say you are given the array {1,2,3,4,3,2,1}: Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

#Let's look at another one.
#You are given the array {1,100,50,-51,1,1}: Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

#Last one:
#You are given the array {20,10,-80,10,10,15,35}
#At index 0 the left side is {}
#The right side is {10,-80,10,10,15,35}
#They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
#Index 0 is the place where the left side and right side are equal.

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
