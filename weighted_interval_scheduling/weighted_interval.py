#  Attempt 1
# def findMaxProfitsNaive(jobs, n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return jobs[0][2]
#     else:
#         return max(jobs[n][2]+ findMaxProfitsNaive(jobs,n-1))
# THIS IS WRONG ALREADY. Because you cannot take job n-1 after you choose n
# You need to find the next job that is possible to match with your current job

# def maxProfitNaive(jobs):
#     pass

# def dfs(jobs, result, results, weights_sum):
#     for i in range(len(jobs)):
#         current_job = jobs[i]
#         job_weight = jobs[2]
#     pass

# Attempt 2


def find_last_non_conflicting_job(jobs, n):
    for index in reversed(range(n)):
        if jobs[index][1] <= jobs[n][0]:
            return index
    return - 1


def find_last_non_conflicting_job(jobs, n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[n][0]:
            # return mid
            # if our finish is less than the start of this job
            # There are 2 cases.
            # case 1 : if this job is the largest index that does not conflict with the current job
            # case 2 : if this job is the NOT the largest index that does not conflict with the current job

            if jobs[mid + 1][1] < jobs[n][0]:
                # to see if mid is the largest index, we see if
                # adding 1 to mid will also ensure that the finish of the
                # candidate job will be less than the start of the current job.
                # If it is, this means that our largest index can be more than the current candidate's one.
                # low += 1
                low = mid + 1
            else:
                # if we know that the current
                return mid

        elif jobs[mid][1] > jobs[n][0]:
            # high -= 1
            high = mid - 1
    return -1


def findMaxProfits(jobs, n):
    if n < 0:
        return 0
    elif n == 0:
        # return the profits from the first job
        return jobs[0][2]
    else:
        next_job_index = find_last_non_conflicting_job(jobs, n)
        # Case 1:
        # include the profit from the current job and add in the
        # the profits from the previous job that has the largest finished index
        # lower than the starting index of the current job.
        include = jobs[n][2] + findMaxProfits(jobs, next_job_index)
        # Case 2:
        # Exclude the current job, and just loo
        # exclude = findMaxProfits(jobs, next_job_index)
        # exclude
        exclude = findMaxProfits(jobs, n-1)
        return max(include, exclude)


def findMaxProfitsMEMO(jobs, n):
    if n < 0:
        return 0
    elif n == 0:
        return jobs[0][2]
    else:
        memo = {}
        if n not in memo:
            memo[n] = findMaxProfits(jobs, n)
        # return findMaxProfits(jobs, n)
        return memo[n]


def findMaxProfitsMEMO(jobs, n):
    memo = {}
    if n not in memo:
        memo[n] = findMaxProfits(jobs, n)
    # return findMaxProfits(jobs, n)
    return memo[n]


def maxProfit(jobs):
    jobs.sort(key=lambda x: x[1])
    print(jobs)
    return findMaxProfitsMEMO(jobs, len(jobs)-1)

# def findMaxProfitsNaive(jobs, n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return jobs[0][2]
#     else:
#         return max(jobs[n][2]+ findMaxProfitsNaive(jobs,n-1))

# def maxProfitNaive(jobs):
#     pass


# each job contains the starting time, ending time, as well as the weights
jobs = [(0, 6, 60), (1, 4, 30), (3, 5, 10),
        (5, 7, 30), (5, 9, 50), (7, 8, 10)]

# the time complexity is O(2^n) because we are
print(maxProfit(jobs))


def maxProfitsBottomUp(jobs, n):
    # sort by the finishing time
    jobs.sort(key=lambda x: x[1])
    dp = [0] * n
    # print(dp)
    # initialize the dp matrix with the first job
    # i.e the job with the least finishing time
    dp[0] = jobs[0][2]
    # for the remaining jobs
    for i in range(1, n):
        # 2 cases: to include and to exclude this CURRENT JOB
        # case 1: to include
        next_job_index = find_last_non_conflicting_job(jobs, i)
        # if there is a next job index
        # ->
        include = jobs[i][2]
        if next_job_index != -1:
            # THE LINE BELOW IS WRONG since now you are using bottom up, you must make use of all the previous values in the DP solution
            # include += jobs[next_job_index][2]
            include += dp[next_job_index]
        # case 2: to NOT INCLUDE
        # THE BELOW LINE IS WRONG, because we are not doing recursion
        # exclude = maxProfitsBottomUp(jobs, n - 1)
        exclude = dp[i-1]
        dp[i] = max(include, exclude)
    return dp[n-1]


print(maxProfitsBottomUp(jobs, len(jobs)))
