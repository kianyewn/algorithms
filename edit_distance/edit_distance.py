class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # let dp[i][j] represent the edit distance from word1[:i] to word2[:j]
        # For example word1 = 'abcd', word2 = 'acbd'
        # we will match word1 = 'a' to word2 = 'a' when j = 0,'ac' when j = 1, 'acb' when j = 2 and so on
        n = len(word1)  # num rows
        m = len(word2)  # num cols

        # YOU ONLY NEED TO INCLUDE THE EMPTY STRING OF WORD2
        dp = [[0] * (m+1) for row in range(n+1)]
        # empty string matching empty string
        dp[0][0] = 0
        for i in range(1, n+1):
            # when word2 = empty string, the number of edit distance is equals to the number of letter in word1
            dp[i][0] = i

        for j in range(1, m+1):
            # when word1 = empty string, the number of edit distance is equals to the number of letters in word2
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                # if the current word match, we look back and see what is the edit distance to do so
                if (word1[i-1] == word2[j-1]):
                    dp[i][j] == dp[i-1][j-1]
                # if it does not match, then there will be three cases
                # i.e if word1[i-1] != word2[j-1]
                else:
                    # when we are trying to delete, replace and insert for edit distance, the edit distance between two words are associative.
                    # i.e word1 edited to word2, or word2 edited to word1 it is the same
                    # "inserting" a letter into word1 is equivalent to "deleting" a word from word2. eg: word1="abdef" - > "ab[c]def", word2="abcdef"
                    # "deleting" a letter from word1 is equivalent to  "inserting" a word into word2. eg: word1="abdef", word2="abcdef" -> "ab[_]def"

                    # (1) insert: think about when will we insert. We will insert if we know that inserting the current letter word2[j-1] will make our word1[:i) + word2[j-1] = word[:j)
                    #         So for example, if word1 = "ab", word2="abc", then we add "c" to word1 so that word1 = "abc"
                    #         Think of this as taking into consideration word1 is shorter than word2, and we need to "insert" letters to make word1 and word2 the same.
                    # if we want to insert the current letter word2[j-1] TO word1[0..i-1], (WRONG then we need to look at dp[i-1][j] + 1), then we need to look at dp[i][j-1] + 1!
                    # Note that we keeping the word1 index the same since we are ADDING/INSERTING a letter to word1. However, since we are adding word2[j-1] to word1, we need to look at the                              previous index of word2.

                    # (2) Delete: think about when will we delete. we will delete if we know that if we delete a letter from word1, we will get word2
                    #         For example, word1 = 'abc', word2='ab', so we need to delete letter "c" from word1 to match word2
                    # if we want to delete our current letter word[i-1], then we need to look back at the previous dp[i-1][j], the reason why we do not have j-1
                    # indexed as the column  is because we are matching the word1[:i-1] up to word2[j]! look at the example above: word1 = 'abc', word2 = 'ab', when we delete
                    # the letter "c" from word1, we are still comparing word1 with the original word2! (also think about it in terms of the double for loop, for i in range for j in range, where each i has each own set of j values as well!)
                    # ------------> dp[i][j] = dp[i-1][j] + 1

                    # (3) Replace: think about when will we replace? since we are using dp, we know that to update dp[i][j],
                    #          this means that all the values dp[0..,i-1][0....,j-1] have the correct correct values already.
                    # if we know that our current word does not match, we try to match our word1 to word2
                    # so, word1 = 'abc', word2='abd', we change word1 to 'abd'
                    # when doing so, we incur a +1 edit distance
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    dp[i][j] = min(insert, delete, replace) + 1
                    # dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    if dp[i][j] == 0:
                        print(insert, delete, replace)
                    #  But what about:
            #  word1 = "abde", word2 = "abcde". edit_distance should be = 1 because i can just insert a "c". OK still works
            #  Eg At index i and j such that word1 = 'ab', and when we match with word2 = 'abc', then insert and then dp[i][j] = dp[i][j-1]+
            #  Eg at index i+1 and j+1 such that word1 = "abd", word2 = "abcd", we see that the word1[i+1] == word2[j+1] == "d", and thus dp[i+1][j+1] = dp[i][j] + **0**
            #  Therefore, in the end, we only have made 1 edit distance!
        print(dp)
        return dp[n][m]
