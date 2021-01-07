#Given a triangle of consecutive odd numbers:

#             1
#          3     5
#       7     9    11
#   13    15    17    19
#21    23    25    27    29
#...
#find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

#odd_row(1)  ==  [1]
#odd_row(2)  ==  [3, 5]
#odd_row(3)  ==  [7, 9, 11]

def odd_row(n):
    
    place_of_first_odd = int(((n-1)*(n))/2) + 1
    odd_in_first_place = (place_of_first_odd *2) - 1
    row = [odd_in_first_place]
    for i in range(2, (n) * 2, 2):
        row.append(odd_in_first_place + i)
    return row
