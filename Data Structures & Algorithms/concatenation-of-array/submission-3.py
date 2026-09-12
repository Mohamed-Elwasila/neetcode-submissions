class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [0] * l * 2

        for i in range(l * 2):
            result[i] = nums[i] if i < l else nums[i-l]
        return result