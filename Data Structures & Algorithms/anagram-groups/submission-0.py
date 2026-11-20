class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            count = [0] * 26 # a to z
            for char in word:
                count[ord(char) - ord("a")] += 1
            hash_map[tuple(count)].append(word)
        
        return list(hash_map.values())