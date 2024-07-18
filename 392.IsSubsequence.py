class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        # Initialize pointers for both strings s and t
        s_init, t_init = 0, 0
        
        # Iterate over both strings until the end of either string is reached
        while s_init < len(s) and t_init < len(t):
            # If characters at both pointers are equal, move the pointer in s
            if s[s_init] == t[t_init]:
                s_init += 1
            # Always move the pointer in t
            t_init += 1
        
        # If s_pointer has reached the end of s, then s is a subsequence of t
        return s_init == len(s)