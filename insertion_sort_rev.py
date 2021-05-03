def swap(lst, i, j):
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp
    return lst


def rev_insertion_sort(lst: list) -> list:
    for i in range(len(lst) - 1, -1, -1):
        current = lst[i]
        # j = i+1
        while i <= len(lst) - 2 and lst[i] < lst[i + 1]:
            lst = swap(lst, i, i + 1)
            i += 1
    return lst


test = [6, 5, 4, 3, 2, 1]
assert rev_insertion_sort([5, 2, 4, 6, 1, 3]) == test, rev_insertion_sort(test)

# test the index


def test():
    s = [1, 2, 3, 45]
    for i in range(len(s), -1, -1):
        print(i)
    return "done"


# print(test())
