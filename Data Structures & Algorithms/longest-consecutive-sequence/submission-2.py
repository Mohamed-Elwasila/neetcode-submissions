class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        nums.sort()
        c = longest = 0

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            if nums[i] - 1 in seen:
                count += 1
            else:
                count = 1

            seen.add(nums[i])
            
            if count > longest:
                longest = count
        
        return longest