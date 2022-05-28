# Brute Force
# Our main task is that after merging ‘ARR2’ into ‘ARR1’.
# The resultant ‘ARR1’ is also sorted. So first we simply add all the elements of ‘ARR2’ into ‘ARR1’. 
# Then we can apply any sorting algorithm to sort ‘ARR1’. 

def ninjaAndSortedArrays(arr1, arr2, m, n):
    
    for i in range(n):
        arr1[i + m] = arr2[i]
        
    arr1.sort()
    return arr1
