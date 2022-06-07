import collections

def majorityElement(arr):
    n = len(arr)

    #in the given array if the majority element should be grater than n/3 that
    #implies there will be max 2elements posiible 3 elements cannot be possible to
    # because 100/3 = 33.33

    freq = collections.OrderedDict() 

    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] +=1

        else:
            freq[arr[i]] =1
    # Iterate through the HashMap.
    for key,value in freq.items():
        # Store all the elements with frequency greater than n/3.
        if value > n/3 :
            majorityElement.append(key)
    # Return all the stored majority elements.
    return majorityElement