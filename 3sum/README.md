# Takeaways

# Attempt 1:
- The first solution i did was a brute force approach with triple for-loop and thus O(N^3) time complexity
  - The important part is to find a way to check for duplicates in the returned solution
    - The way i did this was to use a list containing sets, where each element in the set represents the element in the original array.
      - i.e. set(1,0,-1) == set(0,-1,1).

# Attempt 2:
- The second solution is in O(N^2) time complexity
  - The most important part of this solution is that it uses a sorted array to take care of the duplicates
  - To handle the duplicate, it uses to some sense a bit of combinatorics, where we let each unique element be a starting position, and we search for OTHER UNIQUE numbers AFTER THE INDEX OF THIS STARTING POSITION.
  -  Since are using the beginning of the array as the starting position, and then looking for two sums AFTER the element, and since our array is sorted, we can be sure that once an element is used as a starting position, it will NOT APPEAR AGAIN in the later starting positions, and hence ensue the uniqueness of the threesum
  -  To ensure that the two sums are unique, we similarly make use of the properties of the array, and make sure that whenever we found a solution, we will search for the next low and high index that corresponds to a new unique value.
  - This solution is interesting, because it shows how powerful sorting an array can be 