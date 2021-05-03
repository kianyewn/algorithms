def swap(lst, i, j):
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp
    return lst


def insertion_sort(lst: list) -> list:
    for i in range(len(lst)):
        while i > 0 and lst[i - 1] > lst[i]:
            lst = swap(lst, i, i-1)
            i = i - 1

    return lst


def insertion_sort(lst: list) -> list:
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i+1] = key

    return lst


assert insertion_sort([4, 3, 2, 1]) == [
    1, 2, 3, 4], insertion_sort([4, 3, 2, 1])
