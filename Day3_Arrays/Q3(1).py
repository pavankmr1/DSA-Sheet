def findMajorityElement(arr,n):
    # Declaring dictionary to store the frequency of elements.

    hashMap ={}


    # Iterating each element in the array to count frequencies.
    for i in range(n):

        # Storing frequency of each element.

        if arr[i] not in hashMap:
            hashMap[arr[i]] =1
        else:
            hashMap[arr[i]] +=1

        # If frequency of the element is greater than 'n' / 2, then return the element.
        if hashMap[arr[i]] >n/2:
            return arr[i]

    # If no majority element found, return -1.
    return -1
