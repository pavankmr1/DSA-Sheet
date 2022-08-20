# Using arr.append(curr[:]) means append a COPY of curr while arr.append(curr) append curr itself to the array arr, 
# meaning when you make any change to curr, it's value in arr will also change correspondingly

from typing import*

def rec(st:int, cur: List[int], arr: List[int], subsets:List[List[int]]):
    subsets.append(cur[:])

    for i in range(st, len(arr)):
        if i == st or arr[i] != arr[i-1]:
            cur .append (arr[i])
            rec(i+1, cur , arr, subsets)
            cur.pop
            

def uniqueSubsets(n:int, arr:List[int]) -> List[List[int]] :
    subsets = []
    arr = sorted(arr)
    cur = []
    rec(0,cur,arr,subsets)

    return subsets

