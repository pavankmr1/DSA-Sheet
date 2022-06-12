def MajorityElement(arr):
    n = len(arr)

    majorityElement = []

    firstElement = 0
    secondElement = 0

    firstCount = 0
    secondCount = 0

    for i in range(n):
        if arr[i] == firstElement:
            firstCount += 1

        
        elif arr[i] == secondElement:
            secondCount += 1

        elif (firstCount ==0):
            firstElement = arr[i]
            firstCount =1
        elif (secondCount ==0):
            secondElement = arr[i]
            secondCount =1
        else:
            firstCount -=1
            secondCount -=1

    firstCount =0
    secondCount =0

    for  i in range(n):

        if arr[i] == firstElement:
            firstCount += 1
        elif arr[i] == secondElement:
            secondCount += 1

        if (firstCount >  n/3):
            majorityElement.append(firstElement)
        
        if (secondCount > n/3):
            majorityElement.append(secondElement)

    return majorityElement



