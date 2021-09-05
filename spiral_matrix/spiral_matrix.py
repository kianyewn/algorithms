class Solution(object):

    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        start_row = 0
        end_row = len(matrix) - 1
        start_col = 0
        end_col = len(matrix[0])-1
        res = []
        while (start_row <= end_row) and (start_col <= end_col) and (len(res) != m*n):

            # if start_col <= end_col:
                # move left
            for col_index in range(start_col, end_col+1):
                res.append(matrix[start_row][col_index])
            # if start_row == end_row, then start_row + 1 will make value move_down incorrect
            # since we know that start_row is now > end_row
            start_row += 1

            if start_row <= end_row:
                # move down
                for row_index in range(start_row, end_row+1):
                    res.append(matrix[row_index][end_col])
                # if start_col = end_col, and then we do end_col -= 1, then now start_row > end_col
                # this will make move_right incorrect
                end_col -= 1

                if start_col <= end_col:
                    # move right
                    for col_index in range(end_col, start_col-1, -1):
                        res.append(matrix[end_row][col_index])
                    end_row -= 1
                    # start + 1 and end_row - 1 in the loop, thus we already violate the while loop condition
                    # But since we are still within the while loop, it will only be terminated in the next iteration
                    # This leads to an error when we do (move up), since right now start_row > end_row

                    # move up
                    if start_row <= end_row:
                        for row_index in range(end_row, start_row-1, -1):
                            res.append(matrix[row_index][start_col])
                        start_col += 1

        return res
