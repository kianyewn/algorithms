- This is the question from DBS's interview.

- Takeaways:
  - I had correctly identified this as a dfs problem, where at each state we have two possible values "0" or "1".
  - However, The way I coded the "possible actions from each state" is wrong, as I did a double 'for-loop' which did not make any sense.
  -  This led to infinite loops, and states are not being visited the way I want it to be
  -  To check if the given row_sums and col_sums are possible, when all of the states are visited, I have a solution checker to check if the solution is possible using the conditions that the sum of the solution in axis = 0 (row-wise), is equals to that of the given row_sum, and the sum of the solution in axis = 1 (col-wise) is equals to that of the given col_sum.
     -  Another thing to note regarding this checker is that you cannot do numpy kind of indexing on nested lists, so I cheated a bit and converted my arrays into numpy arrays to have access to them more easily.
