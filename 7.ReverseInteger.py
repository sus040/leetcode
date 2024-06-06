class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Set sign
        if x < 0:
            sign = -1 
        else: 
            sign = 1
        # Reset x as absolute value
        x = abs(x)

        # Reverse the digits of the integer
        reverse = int(str(x)[::-1])

        # Check for 32-bit integer overflow
        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0

        # Return the reversed integer with the original sign
        return sign * reverse