def uniqueElement(arr,n):

    # Declare a HashMap
    hashMap ={}

    # Store frewuency of elements of arrayb in hashmap
    for i in range(n):
        hashMap[arr[i]] = 0
    
    for i in range(n):
        hashMap[arr[i]] += 1
    
    # Find the element having frequency equal to 1 and return it
    for key in list(hashMap.keys()):
        if hashMap[key] == 1:
            return key
    
    pass
