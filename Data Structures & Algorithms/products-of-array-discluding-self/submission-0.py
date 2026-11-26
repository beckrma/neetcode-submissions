class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix suffix technique
        prefix = self.compute_prefix(nums)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]
        return prefix

        
        
    def compute_prefix(self, nums):
        n = 1
        prefix = [1] * (len(nums))
        for index, num in enumerate(nums):
            prefix[index] = n
            n *= num
        return prefix


