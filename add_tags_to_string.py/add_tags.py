def find_starting_index_of_word(word, s):
    """ This code only handles finding the index of the FIRST occurence of the substring word.
    """
    for i in range(len(s)):
        if s[i] == word[0]:
            # "abcdef" vs "bcde"
            if s[i: len(word) + i] == word:
                return i
    # if cannot find return -1
    return -99999999999  # -1


def add_tags(words, s):
    to_bold = [False] * len(s)
    for word in words:
        start_index = find_starting_index_of_word(word, s)
        while start_index >= 0:
            # print(start_index)
            for i in range(start_index, start_index + len(word)):
                to_bold[i] = True
            # if we managed to find the first occurence of the word already, we look for the NEXT FIRST occurence of the word by looking only at the remaining substring
            # termination condition fails since (start_index + len(word) + -1) can be > 0 even if there is no more occurence of the word
            # start_index = start_index + \
            #     len(word) + find_starting_index_of_word(word,
            #                                             s[start_index + len(word) :])
            if start_index + len(word) >= len(s):
                start_index = -1
            else:
                start_index = start_index + \
                    len(word) + find_starting_index_of_word(word,
                                                            s[start_index + len(word):])

            # you cannot do the below statement to find the index of the next occurence..
            # if you change your string to search, then the indexing for "to_bold" will be incorrect, since "to_bold"'s indexing is based
            # on the original string
            # Note: this will also run in infinite loop since you are using the original string "s" in the indexing.
            # For example, consider matching 'abc' with 'abcdefghijabc'.
            #       In the first interation, you have that the starting index is 0,
            #       and then for the NEXT ITERATION, you search through the new remaining substring "abcdefghijabc"[starting_index == 0 + len("abc")==3 -> 3:] == "defghiabc"
            #       and realize that your find_starting_index_of_word("abc", "defghiabc") == 7, which is not the index from the ORIGINAL S
            #       (since it should be starting index 10 for the next occurence of "abc" in "abcdefghijabc" )
            #       Now in the third iteration, you look through "abcdefghiabc" (NOT "defghiabc", since we are using original substring s!) [starting_index==7 + len("abc")==3 -> 10:]
            #       == "abc", and then find_starting_index_of_word("abc", "abc") == 0, and the infinite loop begins all over again!
            # start_index = find_starting_index_of_word(
            #     word, s[start_index + len(word):])

    # at this step, the bold array is already complete, now we only have to add the tags at two places
    # (1) <b> at the element_before is False, the element next is True,
    # (2) </b> at the element_before is True, the element next is False.
    # since we need to check element "before" and element "after", we need to handle two edge cases, of the first and last element separately
    # start = ""
    # end = ""
    # if (to_bold[0] == False) and (to_bold[1] == True):
    # middle ""
    res = ""
    for i in range(len(to_bold)):
        to_add = s[i]
        # since i + 1, the index that we miss out is the last index
        # Therefore this statement will fail to add a "</b>" at the end of the index
        if (i+1 < len(to_bold)) and (to_bold[i] == True) and (to_bold[i + 1] == False):
            to_add = to_add + "</b>"
        # since i-1 , the index that we miss out is the first index
        # Therefore this statement will fail to add "<b>" at the start of the index
        if (i-1 >= 0) and (to_bold[i - 1] == False) and (to_bold[i] == True):
            to_add = "<b>" + to_add
        res += to_add
        # print(res)

    if to_bold[0] == True:
        res = '<b>' + res

    if to_bold[-1] == True:
        res = res + '</b>'
    return res


tc_words = ['abc', 'def', 'efg']
# test "abc" at the beginning only, and that "def" will merge with "efg" to become "defg"
tc_s1 = "abcdefghij"
# test "abc" at the end after not bolding as well
tc_s2 = "abcdefghijabc"

# print(add_tags(tc_words, tc_s1))
print(add_tags(tc_words, tc_s2))
# print(find_starting_index_of_word('bcde', 'abcdef'))
# print(find_starting_index_of_word('bcdie', 'abcdef'))
