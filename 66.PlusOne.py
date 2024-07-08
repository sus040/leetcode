class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Set the range of digits
        n = len(digits)
        # traverse digits in backward
        for i in range(n-1, -1, -1):
            # If digit is less than 9
            if digits[i] < 9:
                # Increment the last digit by 1
                digits[i] += 1
                # Return the last number
                return digits
            # Reset 0 as the last number
            digits[i] = 0
            # Add 1 in the list when digit is greater than 9
            return [1] + digits        