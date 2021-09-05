- One mistake made was thinking that the condition for while-loop will terminate correctly
  - Given the condition (start_row <= end_row) and (start_col <= end_col), you thought that these condition will hold THROUGHOUT THE LOOP, AND THIS IS FALSE
    - The reason is because inside the while loop, we are incrementing start_row, start_col, decrementing end_row, end_col individually. 
      - For example, after we increment start_row(see first condition), we will then use this new_start_row to decrement end_col. (see second condition)
      - Therefore, we needed to **nest the 'if' statements** as shown in my final solution.
      - Doing the if statements un-nested will result in a wrong solution, because some 'if' statements will be executed, while other 'if' statements will not be executed, when the truth is that if one of the condition fails, ALL of the statements should not be executed (we can also see this in the condition for our while-loop, where we use the logic operators "AND")
      - Thus, for my new solution, after incrementing start_row, before executing the next statement, I will check if start_row is less than end_row, and if I decrement my end_col, before executing the next statement, I will check if start_col is still less than end_col.


- Note to myself that my intuition that will happen is also correct, but while working through the solution, I thought that we are EITHER incrementing OR decrementing and then checking if the while-loop condition is still valid.