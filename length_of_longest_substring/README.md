# Takeways

- Method 1
  - The first method that i did was a brute force approach of O(N^2) time complexity since i am trying out all possible substrings that are not duplicated.
    - Since each of the characters at the outer loop at index i can be the start of the substring, i had an inner loop indexed by j that runs from i + 1 until the end of the string. This ensures that i have taken into account all the possible substring, and i only need to check that the substring does not have duplicate. If it does, then the loop is terminated and i just check if the substring is the longest one without repeating characters and move on to the next starting index i + 1.
  - While this solution passed all the test cases, i was not satisfied with the speed (since i am literally iterating through all possible substrings.)

- Method 2
  - The second method that i did was with the intention to optimize the code. Instead of checking for all the possible substrings, a sliding window approach was used.
  - Consider the example "abcadefg". When we look at the string from left to right and saw the second letter "a", we know that the starting index of the new potential substring will be after the first letter "a", i.e. "b".
    - The first letter "a" will NEVER be involved with the new potential substring, since it is replaced by the "second" character.
  - Consider the example "abcabdefg". When we look at the string from left to right, in addition to the duplicated letter "a", there is now also another duplicated letter "b". Similar to the idea before, we know that the new potential substring must be after the first letter "b" or "a", and whoever that comes LAST. This is to ensure that the starting index will ensure that the new potential candidate WILL NOT contain any duplicated letters. Hence, starting index is max(pos(first "b"+1), pos(first "a")+1), and the code will run in O(N) time since we are just using a single loop.