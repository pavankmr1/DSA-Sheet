# In this approach, we will first sort the intervals by non-decreasing order of their start time. 
# Then we will add the first interval to our resultant list. Now, for each of the next intervals, 
# we will check whether the current interval is overlapping with the last interval in our resultant list.
#  If it is overlapping then we will update the finish time of the last interval in the list by the maximum
#   of the finish time of both overlapping intervals. Otherwise, we will add the current interval to the list.

from sys import stdin,setrecursionlimit

class Solution:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def mergeIntervals(intervals):
        n=len(intervals)
        res = []

        for i in range(n):
            curS = intervals[i].start
            curE = intervals[i].end

            # If current interval doesn't overlap with the previous interval.
            if(len(res)==0 or curS> res[len(res).end]):
                res.append(intervals[i])

            else:
                # If current interval overlaps with previous interval.
                res[len(res)-1].end = max(res[len(res)-1].end, curE)

        return res

#main 
n =int(input())
arr1 =list(map(int,stdin.readline().strip().split(" ")))
arr2 =list(map(int,stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []

for i in range(n):
    a=Solution(arr1[i],arr2[i])
    intervals.append(a)

res = Solution.mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start,res[i].end)
