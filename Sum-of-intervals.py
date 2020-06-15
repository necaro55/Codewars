
def sum_of_intervals(intervals):
    
    x, i = 0, 0   
    while x < len(intervals):
        i = 0
        
        if intervals[x] == None:
           
            x += 1
            continue
        while i < len(intervals):
           
            if intervals[i] == None or i == x:
                
                i+=1
                continue
            if not(intervals[x][1] <= intervals[i][0] or intervals[i][1] <= intervals[x][0]):
                
                intervals[x] = ((min(intervals[x]+intervals[i])), (max(intervals[x]+intervals[i])))
                intervals[i] = None
                i = 0           
            i+=1
            
        x += 1
    sum = 0
    for j in intervals:
        if j != None:
            sum += j[1] - j[0]
    return sum
