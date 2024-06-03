class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        # Convert the number to a string
        x_str = str(x)

        # Reverse the string
        return x_str == x_str[::-1]