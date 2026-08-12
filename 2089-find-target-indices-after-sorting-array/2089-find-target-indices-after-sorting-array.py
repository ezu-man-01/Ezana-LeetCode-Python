class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            min_val = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_val]:
                    min_val = j
            nums[i], nums[min_val] = nums[min_val], nums[i]


        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
        
        return output