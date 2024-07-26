class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min(len(s) for s in strs)
        lcp = ""
        for i in range(min_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return lcp
            lcp += char
        return lcp

        