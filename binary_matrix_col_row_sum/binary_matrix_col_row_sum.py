import numpy as np

# RUN dfs on 2 x 3 table
a = [3, 2]
b = [2, 1, 1, 0, 1]

array = np.zeros((len(a), len(b)))
visited = - np.ones((len(a), len(b)))

# This is wrong because we are limited by this counter.
# DFS will need to explore more than len(a) + len(b) ....


def check_array_res(array, a, b):
    # print(array)
    upper_row_check = sum(array[0][:]) == a[0]
    lower_row_check = sum(array[1][:]) == a[1]
    all_true = True
    for col_num in range(len(b)):
        if sum(array[:, col_num]) != b[col_num]:
            all_true = False
    if upper_row_check and lower_row_check and all_true:
        return array
    else:
        return []


def dfs(array, visited, row_num, col_num):
    # print(array, visited)
    # print(visited)
    # print()
    if (row_num > len(a)-1) or (row_num < 0) or (col_num > len(b)-1) or (col_num < 0):
        return []

    if len([visited[row][col] for row in range(len(visited)) for col in range(len(visited[0])) if visited[row][col] < 0]) == 0:
        return check_array_res(array, a, b)

    if visited[row_num][col_num] < 0:
        visited[row_num][col_num] = 1
        for value in [0, 1]:
            array_cp = array.copy()
            array_cp[row_num][col_num] = value
            visited_cp = visited.copy()
            move_left = dfs(array_cp, visited_cp, row_num, col_num-1)
            move_right = dfs(array_cp, visited_cp, row_num, col_num+1)
            move_down = dfs(array_cp, visited_cp, row_num+1, col_num)
            move_up = dfs(array_cp, visited_cp, row_num-1, col_num)
            if len(move_left) > 0:
                return move_left
            if len(move_right) > 0:
                return move_right
            if len(move_down) > 0:
                return move_down
            if len(move_up) > 0:
                return move_up

    return []


dfs(array, visited, row_num=0, col_num=0)
