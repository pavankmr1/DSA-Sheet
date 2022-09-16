def median(a,b):

    n = len(a)
    m = len(b)
    i = j=m1=m2=0

    # Find median

    for count in range((n+m)//2 +1):

        m2 = m1

        if i !=n and j!=m:

            if a[i] >b[j]:
                m1 = b[j]
                j+1
            
            else:
                m1 = a[i]
                i+1
        
        # If i is less than n
        elif i<n:
            m1 = a[i]
            i+=1
        
        else:
            m1=b[j]
            j+=1
    
    # Check if sum of n and m is even
    if (n+m)%2:
        return m1*1.0
    
    return (m1+m2)/2

