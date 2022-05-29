# Greedy Approach
# As we know both ‘ARR1’ and ‘ARR2’ are sorted. So we can declare two variables ‘i’ and ‘j’ and initialize ‘i’ with ‘M’ and ‘j’ with ‘N’.
#  Then we compare the last element of both arrays/lists and we insert the larger element to the end of the ‘ARR1’.
#   We continue this process while all the elements of ‘ARR2’ are not merged into ‘ARR1’. 

def ninjaAndSortedArrays(arr1, arr2, m, n):
    i =m-1
    j =n-1
    lastIndex = m+n-1

    while j>=0:

        if  i>=0 and arr1[i]>arr2[j]:
            arr1[lastIndex] = arr1[i]
            i -=1

        else:
            arr1[lastIndex] = arr2[j]
            j-=1
        lastIndex -=1
    return arr1 