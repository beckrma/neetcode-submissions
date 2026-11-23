class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = defaultdict(int)
        freq=[[] for n in range(len(nums) + 1)] # not using index 0, add one to end
        for num in nums:
            hash_table[num] += 1
        for number, count in hash_table.items():
            freq[count].append(number)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res