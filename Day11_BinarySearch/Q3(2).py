def uniqueElement(arr,n):   

    # Declare a variable to store answer and intialise its value to zero
    answer =0

    # Do xor of all elements and store the result in answer
    for element in arr:
        answer ^= element
    
    return answer

    pass