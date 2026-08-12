class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_val = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_val]:
                    min_val = j
            nums[i], nums[min_val] = nums[min_val], nums[i]