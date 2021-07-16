class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        results = []
        for i in range(len(s)):
            subsequence = s[i:i+10]
            if subsequence not in dic:
                dic[subsequence] = 0
            dic[subsequence] += 1
            if (dic[subsequence] > 1) and (subsequence not in results):
                results.append(subsequence)
        return resultsi
