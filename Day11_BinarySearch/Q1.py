def findNthRootOfM(n: int, m: int) -> float:

    # Intialize the variable 'low'
    low =0

    # Intialize the variable 'high'
    high =m

    # Intialize the variable 'eps'
    eps = 1e-7

    # Binary search algorithm.
    while high-low > eps:

        # Intialize the variable 'middle'
        middle = (low+high)/2

        # Intialize the variable 'exp'
        exp = pow(middle, n)

        # Check if 'exp' is equal to 'm'.
        if exp<m:
            low = middle
        else:
            high = middle
    return format(low,".6f")