class Solution(object):
    # Method 1 
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # since i did a i+1, it is possible that the length of the input string is length 1, and it will not work
        if len(s)==1:
            return 1
        
        longest_substring = ""
        for i in range(len(s)):
            substring = s[i]
            longest_substring = update_longest_substring(substring, longest_substring)
            # since i did a i+1, it is possible that the length of the input string is length 1, and it will not work
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    longest_substring = update_longest_substring(substring, longest_substring)
                else:
                    break
        print(longest_substring)
        return len(longest_substring)
                    
                    
                
    def update_longest_substring(candidate, longest_substring):
        if len(candidate) > len(longest_substring):
            longest_substring = candidate
        return longest_substring

    # Method 2
    def lengthOfLongestSubstring(self, s):
        # "start" denotes the position of the starting index position of the substring
        # hm to keep track of the current index position of the character in the candidate substring. We use hm to update the "start" position. For example, if a character is seen in the hashmap already, then we consider the new "start" of the new candidate substring as start + 1. This is because the character in the old "start" position will never be part of the new potential longest substring with the new "start. Eg: "abcdaefg"
        start = 0
        hm ={}
        longest_substring_length = 0
        for i in range(len(s)):
            current_char = s[i]
            # if contains repeating characters
            if current_char in hm:
                # We use max because for example, if there are 2 repeating characters "a" and "b" in "abcbaefg", we need to ensure that our "start" position does not contain ANY of the  2 duplicated letters.
                
                start = max(start, hm[current_char]+1)
                
            hm[current_char] = i
            candidate_length = i - start +1# trace the example "abcbaefg"
            if candidate_length > longest_substring_length:
                longest_substring_length = candidate_length
        return longest_substring_length