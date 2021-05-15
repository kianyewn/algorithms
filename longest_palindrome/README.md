# Takeways
- Attempt 1
  - The first attempt was the brute force approach, where the goal was to look for all possible palindromes. This is achieved by using every character in the string as a possible start for the palindrome, and then iterate through the rest of the characters(after the start position). So what this is doing is that i am looking at all possible substring, and then checking whether or not the original substring and the reversed substring is the same.
  - One mistake and takeaway even for this simple brute force method is that since i am using the indexes to slice my array, I needed to increase the range that my index i runs through, so that I can capture the entire array (since the index i in arr[:i] is non-inclusive!)
  
  - The most important takeaway is that I originally thought that this was an O(N^2) method, since I was only using 2 for loops (nested), and failed to see that the way i checked whether my substring is a palindrome took an additional factor of O(N) as well, which made the time complexity O(N^3)! This is something that I totally forgot about!
  - This solution passed the test cases, and the only time it failed was due to time limit exceeded

- Attempt 2
  - The second attempt that I did was to try and preprocess the string such that I have a forward_string as well as a backward(revered) string.
  - I was too excited and thought that this problem is very easy, in that all i needed to do was to check that for i in range (1 to len(string)+1), forward_string[:i] is equals to backward_string[-i:]
  - This is actually wrong because I am only considering index 0 as the start of the possible start substrings!
  - What i learnt was also that if I were to have a forward and backward type of the same string, the index that i used for slicing both the strings had to start from 1 and end at length of the string(inclusive). The code was very simple and this made me appreciate the fact that the creators of python used string[-1] to denote as the last element of the string.


- Attempt 3
  - The third attempt was an attempt to draw inspiration from the "longest substring without duplicate" problem. Since I needed to find substrings, I though that i can reuse the idea of using hashmaps to denote the starting position of a possible substring
  - However, this definitely did not work. The idea of using the hashmap worked for the "longest substring without duplicate" problem is because if the starting position is not the longest substring without duplicate, it will never ever be part of the longest substring. Consider the string "abcads". After iterating through the string and realizing that there is a second "a", the first "a" will never ever be part of the later possible longest substrings anymore. In the case of this longestPalindrome problem, if the starting position is currently not part of the longestPalindrome problem, the same starting position CAN BE the start of the actual longest palindrome. consider "abba", where the start of the longest palindrome is the first "a"!

- Attempt 4
  - This attempt was inspired by the solution on leetcode haha, and uses the property of a palindrome, and i thought that i can see the connection and thought process of how people think about algorithms
    - As mentioned in the first attempt, the issue for the time complexity comes from the fact that checking the palindrome takes O(N) time. So for this solution, the main difference is that it provides an optimized way to check for palindrome, in that we are looking at substrings and checking whether substrings are palindromes **AT THE SAME TIME!**
  - I realized that it is completely fair game to use the properties of a concept to optimize your code: for a palindrome, there is two possible centers. For example, a palindrome can be expanded outwards on both left and right direction at  "b" or "bb". 
  - Using this property, we just had to iterate through all possible cases of "b" and "bb" in the original string, and find the one (out of the two cases) that is the longest
  - For example reason, the suggested solution returned the length of the palindrome eventhough they could have made things a lot simplier, and return the actual palindrome like i did.
    - For their solution, i also learn to take into consideration what the final value of your indexes will be after the while loop terminates
      - For example, the indexes will always be +1 or -1 outside the allowed values, which leads to the termination of the while loop.
        - Therefore the author actually used (RIGHT - LEFT - 1), which can be quite different from what we see. try it with "xabbayz"!