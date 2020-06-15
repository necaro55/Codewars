def odd_row(n):
    
    place_of_first_odd = int(((n-1)*(n))/2) + 1
    odd_in_first_place = (place_of_first_odd *2) - 1
    row = [odd_in_first_place]
    for i in range(2, (n) * 2, 2):
        row.append(odd_in_first_place + i)
    return row
