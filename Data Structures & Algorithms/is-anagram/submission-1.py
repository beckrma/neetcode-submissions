class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        
        for letter in t:
            if letter not in hashmap:
                return False
        
            hashmap[letter] -= 1

            if hashmap[letter] < 0:
                return False
        return True