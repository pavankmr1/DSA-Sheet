def ninjAndLadoos (row1, row2,m,n,k):

    sortedRows = [0]*(m+n)

    a,b,c = 0,0,0

    # Iterate while a is less than m and b is less than n
    while a<m and b<n:
        if row1[a]<row2[b]:
            sortedRows[c] = row1[a]
            a+=1
        
        else:
            sortedRows[c] = row2[b]
            b+=1
        
        C+=1
    
    # Iterate whilw a is less than m
    while a<m:
        sortedRows[c] = row2[b]
        a+=1
        c+=1
    
    # Iterate while b is less than n
    while b<n:
        sortedRows[c] = row2[b]
        b+=1
        c+=1
    
    return sortedRows[k-1]
    pass
