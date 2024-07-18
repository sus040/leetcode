class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initiate first order of number
        max_current = max_global = nums[0]
        # Iterate through a input list
        for num in nums[1:]:
            # Return max number 
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        # Return its sum
        return max_global