def ninjaAndLadoos(row1,row2,m,n,k):

    i=0
    j=0

    # Iterate while i is less than m and j is less than n
    while i<m and j<n:

        if i+j == k-1:
            return min(row1[i], row2[j])
        
        if row1[i] < row2[j]:
            i+=1
        else:
            j+=1
    
    # Iterate while i is less than m
    while i<m:
        if i+j == k-1:
            return row1[i]
        i+=1
    
    # Iterate while j is less than n
    while j<n:
        if i+j == k-1:
            return row2[j]
        j+=1
    
    # Tis line never runs because we get our desired k inthe above code
    return row2[i+j]
    pass
