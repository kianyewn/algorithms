# Takeaway

- I had met this question several times and always wanted to cry.

- The way to approach this method is to use a 2-d matrix, where the rows represent the characters in the string, and the columns represent the characters in the regular expression.
  - if we use index i to represent the character in the string, and j to represent the current character in the regular expression,then the 2-d matrix represents the matching of the string s[:i] with each regular expression r[:j]
  - The problem and difficulty lies with the "\[a-z\]*" expression, where we have to handle three different cases:
    - 1. Empty match
      - For example s = "ba", r ="bag*". When we encounter "*", we need to look back at the preceding element to see if the preceding character at position j-1 is the same as the current character at position i. Since "a" and "g" does not match, we look back TWO STEPS(two because of the asterisks and preceding element) matrix[i][j-2], where we are still in the current row position i, just that we are matching the case of "what if our regular expression do not have g*"
      - 2. Single match
        - For example s='bag', r='bag*'. When we encounter "*", we need to look back at the preceding element and see if the preceding element at position j-1 is the same as the current character at position i. Since we see that 'g' is the same as the preceding element in "g*", we look back only at the preceding element matrix[i][j-1], where we are still in the current row position i, and col position j-1.
          - Note that matrix[i][j-1] will have already been populated, since we are now at index j.
      - 3. Multiple matches
        - For example, s = 'aa', r='a*'. When we encounter "*", we need to look back at the preceding element and see if the preceding element at position j-1 is the same as the current character at position i. Since we know that 'a' is the same as the preceding element in 'a*'.
          - Note that we cannot use the "Single match" method where we let matrix[i][j] = matrix[i][j-1].
            - The reason is because when we look at the preceding character, we are matching s='aa' with r ='a', and this is equivalent to matrix[i][j-1] which is False.
            - The correct way is to think about us removing the additional character in s, such that s = 'a', and compare it with the already calculated r ='a*', such that matrix[i][j] = matrix[i-1][j]
          - Note that you can actually use this formula to handle the "single match" formula, i.e. remove this "# or (matrix[i][j-1]) " from the code.
            - The reason is that multiple matches is a stronger form, and matching a single character is just a special case of multiple matches. 
- This question is a DP problem, and highlights the importance of being able to play around with the indices of the matrix.