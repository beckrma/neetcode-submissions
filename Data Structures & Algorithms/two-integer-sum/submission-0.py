class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_hash = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in output_hash:
                return [output_hash.get(difference), index]
            else:
                output_hash[num] = index