class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()

        for n in nums:
            if n in answer:
                return True
            answer.add(n)
        return False