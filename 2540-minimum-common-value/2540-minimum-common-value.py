class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        common = list(set(nums1) & set(nums2))
        if common == []:
            return -1
        else:
            smallest = min(common)
        return smallest