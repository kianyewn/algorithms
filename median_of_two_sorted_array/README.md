# Takeway

- The solution that I adopted was using the "merge" algorithm

- This solution will not guarantee a time complexity of O(log(m+n)) which was required by the question, but nonetheless it is faster than 70%++ of other submissions, and most importantly, there are quite a few things that i learnt along the way(and I really like the fact that I am able to code what I am thinking reliabily, and learn from the gaps in my logic)

- Things learnt:
  1. Since I am using the index of two arrays to terminate the "merge" solution, there needs to be code to handle the situation where either of the arrays are empty. If I do not do so, my while statement will never run, and the default result will be returned. I am really pleased to be able to handle this situation using the idea of sentinels, where an infinite value proxy is added to the end of the array. The logic is simple:By adding an infinite value at the end, this means that it will be guaranteed that none of the array is empty. Moreover, since the value added is infinite, the value will only be added into the merged array after the original values in the other array have been added into the merged array, which ensures that the final merged sorted array is correct.

  2. While doing up the solution, I realized that the sum of the two indexes created for both array i+j is equals to the number of elements being inserted into the merged array. This is used to create a shortcut, whereby the the median is returned when we know that the median number has already been added into the merged array. This means that we do have to sort the entire array.

  3. Another optimization is for the space. Instead of creating a new array to store the entire merged array, I just used two variables to keep track of the current second largest number(m1) and the current largest number(m2). Two numbers are stored in memory because this is to handle the case where the sum of lengths of two the two arrays are even numbers, and therefore, we need to sum the 2 numbers that lie around the middle of the hypothetical merged array. If the sum of the two numbers is odd, it is simple such that when the sum of our indexes i and j equals to the number that lie in the middle of the hypothetical merged array, the current number is the median value.

- Alternative solution:
- Main idea is to skip the merging of the two sorted arrays together.
  - The alternative solution uses binary search to find the index to partition the merged array into "left" and "right" partitions, where all the values in the "left" parition is less than or equals to the "right" partition
  
  - This is done by using the smaller array as the input to the binary search, and also using the idea that the median is at the half_length(half the sum of the length of the 2 arrays) position. The trick is to create dependencies between two indexes i and j, where i is the index that decides how much of arr1 is in the "left" partition, and (j = half_length - i) is the index that decides how much of arr2 is in the "right" partition.
    - The binary search makes use of the idea that we want to find a parition in arr1, such that for every element in arr1[:i] and arr2[:j] is less than or equals to arr1[i:] and arr2[j:]!
  
  - Note that if we were to use the formula (j = half_length - i), we have to ensure that j will always be positive, and this is where using i to represent the smaller array is extremely important!

  - The main difficulty in understanding the different edge cases
    - When i == 0, j == 0, i == m, j == n, and what if i != 0, j != 0, i != m, j != n
    - Basically there are three cases
    - 1. if i == 0 or j == 0:
      - if i == 0, NONE of the elements in arr1 are inside the "left" partition
        - then the maximum value in the "left" partition must be arr2[j-1]
      - if j ==0, NONE of the elements in arr2 are inside the "left" parition
        - then the maximum value in the "left" partition must be arr1[i-1]
    - 2. if i == m or j == n:
      - if i == m, ALL of the elements in arr1 are inside the "left" partition
        - then the minimum value in the "right" partition must be arr2[j]
      - if j == n, ALL of the elements in arr2 are inside the "left" partition
        - then the minimum value in the "right" partition must be arr1[i]
    - 3. if i != m or j != n or i != 0 or j != 0:
      - then maximum value in the "left" parition = max(arr1[i-1], arr2[j-1])
      - then minimum value in the "right" = min(arr1[i], arr2[j])