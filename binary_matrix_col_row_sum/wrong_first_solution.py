import numpy as np
a = [3, 2]
b = [2, 1, 1, 0, 1]

ans = [[1, 0, 1, 0, 1],
       [1, 1, 0, 0, 0]]
# FAIL-ed !


def check_array_res(array, a, b):
    upper_row_check = sum(array[0, :]) == a[0]
    lower_row_check = sum(array[1, :]) == a[1]
    all_true = True
    for col_num in range(len(b)):
        if sum(array[:, col_num]) != b[col_num]:
            all_true = False
    return upper_row_check and lower_row_check and all_true


visited = np.zeros((len(a), len(b)))
array = np.zeros((len(a), len(b)))


def dfs(array, visited, a, b, traversed=0):
    # fill = 1
    # fill = 0
    if check_array_res(visited, a, b):
        return True
    if traversed == len(a) + len(b):
        return False

    for i in range(len(a)):
        for j in range(len(b)):
            if visited[i][j] == 0:
                for value in [0, 1]:
                    array_cp = array.copy()
                    visited_cp = visited.copy()
                    array_cp[i][j] = value
                    visited_cp[i][j] = 1
                    res = dfs(array_cp, visited_cp, a,
                              b, traversed=traversed+1)
                    if res == True:
                        return array
    return "impossible"


a = [4, 2]
b = [2, 1, 1, 0, 1]
dfs(array, visited, a, b)


# Also implemented the checking of the matrix wrongly
a = [3, 2]
b = [2, 1, 1, 0, 1]

ans = np.array([[1, 0, 1, 0, 1],
                [1, 1, 0, 0, 0]])
# FAIL-ed !


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
    # return upper_row_check and lower_row_check and all_true


check_array_res(ans, a, b)
