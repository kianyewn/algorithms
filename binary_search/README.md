# Takeaways
- A quick recap on binary search.
- One thing i tried to do was to use recursion to find the index of the value to be found.
  - for example, nums = [0,1,2,3] nums[2:] = [2,3], the element 2 is located at index 2 in nums, while element 2 is located at index 0 in nums[2:]. 
  This lead to the discrepancy in the results.
  - However, if we were to return just the value, it will be fine, and the time complexity will still be O(log(n))