def findMajorityElement(arr,n):
    # Variable to store the majority element in the array, it it is present.
    majorityElement =-1
    count =0

    # Iterating the array to know if there is a possible majority element present.
    for i in range(n):

        # If count becomes 0, set current element as a possible candidate for majority element, reset count to 1.
        if count ==0:
            majorityElement =arr[i]

        # Increment the count if the current element of the array is equal to the current majority element, else decrement it.
        if arr[i] == majorityElement:
            count += 1
        else:
            count -= 1

    count =0

    # Checking if majority element occurs more than 'n' / 2 times.
    for i in range(n):
        if arr[i] == majorityElement:
            count += 1

    # If the count of the majority element is greater than 'n' / 2, then return it.
    if count > n/2:
        return majorityElement

    # If no majority element found, return -1.
    return -1
