def ninjaAndLadoos(row1,row2,m,n,k):

    # IF the length of first array is smaller than length of second then swap boththe arays
    if m>n:
        return ninjaAndLadoos(row1,row2,n,m,k)
    if m==0:
        return row2[k-1]
    
    # If k is equal to 1
    if k==1 :
        return min(row1[0],row2[0])
    
    i = min (m,k//2)
    j = min (n,k//2)

    # If row1[i-1] is greater than row2[j-1]
    if row1[i-1] > row2[j-1]:
        newRow2 = row2[j:]
        return ninjaAndLadoos(row1, newRow2,m,n-j,k-j)
    
    newRow1 = row1[i:]

    return ninjaAndLadoos(newRow1,row2,m-i,n,k-i)

    pass
