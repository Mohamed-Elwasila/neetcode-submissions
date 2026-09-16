class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        res = [1] * len(nums)
        
        m = 1

        for i in range(len(nums)):
            pre[i] = m
            m *= nums[i]

        m = 1

        for i in range(len(nums)-1, -1, -1):
            suf[i] = m
            m *= nums[i]
        
        for i in range(len(nums)):
            res[i] = pre[i] * suf[i]
        
        return res