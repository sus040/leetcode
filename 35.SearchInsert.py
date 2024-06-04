class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type: int
        """
        # Traverse index of input number
        for i in range(len(nums)):
            # Return index
            if nums[i] >= target:
                return i
        return len(nums)