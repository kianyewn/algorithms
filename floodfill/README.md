- I was too used to doing DFS and BFS using the "Node Class" and forgot how to traverse a grid or 2-d matrix.
- When we get a 2-D matrix, think of it as a checkboard.
    - Then, the solution is just to use dfs and the possible set of moves at each time step are determined by increment and decrement the row and col indexes accordingly so that they corresponds to "move_left", "move_right", "move_up", "move_down", or any other kind of movements permitted by the question
    - The key thing is also to ensure that incrementing or decrementing does not lead to index out of range for the board.
- The use of visited is an easy way to keep track of the current (x's,y's) used.
  