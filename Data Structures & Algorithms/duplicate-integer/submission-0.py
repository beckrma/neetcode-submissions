class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = set()
        for num in nums:
            if num in my_hash:
                return True
            else:
                my_hash.add(num)
        return False 