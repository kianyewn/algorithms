class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        longest_palindrome = ""
        # lst[1:1] is empty string. so the following code will fail, which is the reason why we need to have an edge case to handle string of length 1.
        for i in range(len(s)):
            # i need to plus 1 in the loop range, because j is used to actually used as the ending index  when slicing.
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                # NOTE  THIS IS NOT AN O(N^2) SOLUTION THAT YOU FIRST THOUGHT
                # The reason is that the checking of the solution is O(N)
                # and therefore the 2 outer loop O(N^2) * O(n) becomes O(N^3)!
                # This is something that I forgot, but very crucial!!!
                if (substring == substring[::-1]) and (len(substring) > len(longest_palindrome)):
                    longest_palindrome = substring

        return longest_palindrome

    def longestPalindrome(self, s):
        # this entire code is wrong because you did not take care the starting position of the possible palindromes.
        # this solution assumes that the palindrome begins at index 0 only, since you are only looking at the ending index i when slicing the string.
        reversed_s = s[::-1]
        longest_palindrome = ""
        for i in range(1, len(s)+1):
            forward_substring = s[:i]
            backward_substring = reversed_s[-i:]
            if forward_substring == backward_substring and len(forward_substring) > len(longest_palindrome):
                longest_palindrome = forward_substring
        return longest_palindrome

    def longestPalindrome(self, s):
        hm = {}
        start_pos = 0
        longest_palindrome = ""
        for index, char in enumerate(s):
            # this method is wrong, because if the current hm[char] is not the start of a current palindrome, there is still a chance that it is the start of the longest palindrome in the end. For example "abba".
            if s[start_pos:index] != s[start_pos:index][::-1]:
                start_pos = max(start_pos, hm[char]+1)
            hm[char] = index
            if (s[start_pos:index] == s[start_pos:index][::-1]) and (len(s[start_pos:index]) > len(longest_palindrome)):
                longest_palindrome = s[start_pos:index]
        return longest_palindrome

    def check_palindrome(self, s, start, end):
        i = start
        j = end
        # since we are substracting i, we ensure that i >= 0, and since we are adding j, we ensure that j is  < len(s)
        # then we expand from the start and end
        while (i >= 0 and j < len(s)) and (s[i] == s[j]):
            i -= 1
            j += 1

        # return the length of the palindrome obtained from this starting and ending position
        # for example, xabbay = (R = 5 - L=0 - 1) = 4 for result "abba"
        return s[i+1:j]

    def longestPalindrome(self, s):
        # since i know that the issue of O(n^3) comes from the way i ineffectively check for a palindrome, we use the method of expanding from center by exploiting the property of a palindrome
        longest_palindrome = ""
        for i in range(len(s)):
            # palindrome that starts from one character, eg 'a' and expand onwards
            candidate1 = self.check_palindrome(s, i, i)
            # palindrome that starts from two characters, eg 'bb' and expand onwards
            candidate2 = self.check_palindrome(s, i, i+1)
            best_candidate = candidate1 if len(
                candidate1) > len(candidate2) else candidate2

            if len(best_candidate) > len(longest_palindrome):
                longest_palindrome = best_candidate
        return longest_palindrome
