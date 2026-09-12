class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) * 2
        result = [0] * length

        for i in range(length):
            result[i] = nums[i] if i < len(nums) else nums[i-len(nums)]
        return result