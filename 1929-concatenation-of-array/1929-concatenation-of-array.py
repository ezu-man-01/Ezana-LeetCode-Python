class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        add = []
        for i in range(len(nums)):
            add.append(nums[i])

        ans = nums + add
        return ans
