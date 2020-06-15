def up_array(arr):
    
    arr.reverse()
    pow_ten = 10
    if len(arr) == 0 or arr[0] < 0 or arr[0] >= 10:
        return None
    arr[0] += 1
    for i in range(1,len(arr)):
        if arr[i] < 0 or arr[i] >= 10:
            return None
        arr[i] *= pow_ten
        pow_ten *= 10
    a = [int(x) for x in str(sum(arr))]
    

    return a
