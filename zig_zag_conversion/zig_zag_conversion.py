def convert(s, numRows):
    if numRows == 1:
        return s
    step = -1
    curr_index = 0
    result = [""] * numRows
    for char in s:
        result[curr_index] += char
        if (curr_index == numRows - 1) or (curr_index == 0):
            step = -1 * step
        curr_index += step
    return "".join(result)


def print_zigzag(string, r):
    current = ""
    result = ["" for i in range(r)]
    diag = False
    for i in range(len(string)):
        current_char = string[i]
        current += current_char
        # note that this condition only runs when the length of our "current" string is of length r
        # it is possible that the loop will terminate if "current" will contain some characters but not yet of length r
        # for example if r = 5 and string = "abcdef", then the first batch of "current" will be 'abcde',
        # and the second batch of "current" will only be 'f', and thus the need to handle this edge case later.
        if len(current) == r:
            if diag == True:
                for j in range(len(current) - 1, -1, -1):
                    # if diag is true, we do not add in the first and last index since
                    # the same elements are already added when diag is False
                    if (j != len(current)-1) and (j != 0):
                        result[r-1-j] += current[j]

            elif diag == False:
                for j in range(len(current)):
                    result[j] += current[j]

            # if the length of "current" is r, then we switch the opposite of the current movement
            diag = not diag
            # if the length of "current" is r, we keep the first character
            current = current_char

    # handle the edge case where "current" contains letters
    if len(current) > 0:
        if diag == True:
            for j in range(current):
                # we can remove (j != len(current) - 1) since we know definitely that the r-th character is not inside the "current"
                if (j != 0):
                    result[r-1-j] += current[j]
        elif diag == False:
            for j in range(len(current)):
                result[j] += current[j]
    print(result)
    return "".join(result)


string = "PAYPALISHIRING"
r = 3
print(print_zigzag(string, r))
r = 4
print(print_zigzag(string, r))
print(convert(string, r))
