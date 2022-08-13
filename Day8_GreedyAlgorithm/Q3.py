'''Where N is size of the array "jobs" and maxDeadline is the maximum among all the deadlines.'''
def jobScheduling(jobs):

    jobs.sort(key=lambda x: (-x[1],-x[0]))
    maxProfit = 0
    maxDeadline = 0

    # Find the maximum deadline among all the jobs
    for i in range(0,len(jobs)):
        maxDeadline = max(maxDeadline,jobs[i][0])
    
    # create a slots list of size maxDeadline + 1
    slots = []

    # Initialise the array to false intially
    for i in range(0,maxDeadline+1):
        slots.append(False)
    
    maxProfit = 0
    for i in range(len(jobs)):
        x = jobs[i][0]
        while x > 0:
            if slots[x] == False:
                maxProfit = maxProfit + jobs[i][1]
                slots[x] = True
                break
            x -=1
    
    return maxProfit
    