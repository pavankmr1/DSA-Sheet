def median(a,b):

    # combine the array
    c = a+b

    c.sort()

    # Find the median
    l= len(c)

    if l%2==0:
        ans = c[l//2 -1] + c[l//2]
        return  ans/2
    
    return c[l//2]
    