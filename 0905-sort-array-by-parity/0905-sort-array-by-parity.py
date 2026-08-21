class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first, second = 0, 0

        while second < len(nums):
            if nums[second] % 2 == 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1

            second += 1

        return nums