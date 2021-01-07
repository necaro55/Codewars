#Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

#Intervals
#Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

#Overlapping Intervals
#List containing overlapping intervals:

#[
#   [1,4],
#   [7, 10],
#   [3, 5]
#]
#The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
#
#Examples:
#sumIntervals( [
#   [1,2],
#   [6, 10],
#   [11, 15]
#] ); // => 9
#
#sumIntervals( [
#   [1,4],
#   [7, 10],
#   [3, 5]
#] ); // => 7

#sumIntervals( [
#   [1,5],
#   [10, 20],
#   [1, 6],
#   [16, 19],
#   [5, 11]
#] ); // => 19

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
