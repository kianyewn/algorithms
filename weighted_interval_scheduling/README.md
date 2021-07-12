# Takeaways
This section marks the starts the end of my break.

1. Attempt1
- I was not able to come up with a solution to this problem and had to look for the solution to the get go.
- The reason why this is different from a typical DFS or BFS solution to find the optimal solution is because we needed to make sure that if we choose a particular job, it affects the jobs that we can take in the next depth.
- I had forgotten how to deal with this situtation, but nonetheless, it is a good exposure for me to learn how to modify the search space of my search algorithm.

2. Attempt2
- The first thing that i needed to solve was how do i modify the search space for my search algorithm. the solution did it by:
  - 1. Sort the jobs according to the finishing time
    - So why do we sort by the finishing time, and not the starting time?
      - The reason is because we are choosing the job with the longest finishing time first.
      - After we have chosen the job with the largest finishing time, we proceed to choose the choosing the NEXT job available with the largest finishing time that does not exceed the starting time of the currently chosen job. 
         - For example, if the job with the longest finishing time is at 5pm, and its starting time is 2 pm, we cannot expect to choose another job that is from 1pm to 3pm because it will overlap.
   - 2. After sorting the jobs, if we decide to choose the current job 'n', then we through our sorted jobs from the end to the beginning, so that when we first find a job with a finishing time less than the starting time of job 'n', it will be the job with the largest finishing time that is non-conflicting again.
   - Note also that if we do not do this, then the time complexity of our search will be exponential O(2^n), since our branching factor is 2.


- Then it is simple, we have 2 base cases to find the optimal solution. We let OPT(n) stands for the optimal solution if we chose job n.
  - 1st base case:
    - if n < 0, this means that there is no job, so we can just return 0
    - Note that this is important, because in our find_last_non_conflicting_job(jobs,n), if we cannot find a job, we return '-1'. This means that if we did not find a next job, then we add back 0, which is exactly what we wanted.
  - 2nd base cas:
    - if n == 0, this means that we are choosing the first job, so we choose the weight associated with the first job


- After establishing our 2 bases, we find the maximum from 2 cases:
   1. if we choose job 'n', then we add the weight associated with job 'n' as well as the OPT of choosing the next non-conflicting j.
      - weight(n) + OPT(next_non_conflicting_job(n))
  2. if we DO NOT choose job 'n', then we look for the NEXT and not necessarily non conflicting job 'n-1'.
      - OPT(n-1)

3. Other improvements to the algorithm include using memoization
  - This helped me to remember that memoization is just a way for us to keep track of things that we had calculated. we do not have to modify the original function.
    - For example, in this code, instead of doing memoization in the findMaxProfits(jobs, n), i can just create a wrapper findMaxProfits(jobs, n) to help speed up the time complexity.

4. Using the BottomUp approach is also where we use a list to keep track of the best choices of the jobs
   1. we initially initialize the array dp[0] with the weight from the first job, and then subsequently find the optimal solution by comparing between maximum(weight(i) + dp[next_non_conflicting_job(i)], dp[i-1])
   2. Note that we need to keep in mind that it is possible that we there is no next conflicting job for one particular job
      1. This is handled by our base case in our recursion, but since this is an iterative approach, we need to take care of this situation ourselves.


5. The last optimization speeds up the way we find the index of the last non conflicting job. 
   1. The original way that we did was to loop through the entire array, which can take O(n) time.
   2. However, remember that anytime we need to find something in a sorted array, we can always use a binary search approach, which was the optimization used.