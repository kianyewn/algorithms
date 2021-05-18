def isMatch(s, p):
    matrix = [[False] * (len(p) + 1)] * (len(s) + 1)
    return matrix


print(isMatch('abc', 'abc'))
