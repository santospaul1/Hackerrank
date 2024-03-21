
def median(arr):
    arr.sort()
    x = len(arr)
    
    if x%2 == 0:
        median1 = arr[x//2]
        median2 = arr[x//2-1]
        median = (median1 + median2)/2
        return median
    else:
        
        return arr[x//2]
 
list = [3,22,4,8,6,8]
print(median((list)))
