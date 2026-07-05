class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for char in magazine:
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1
        for char in ransomNote:
            if char in count:
                count[char] = count[char] - 1
            else :
                return False
        for val in count.values():
            if val < 0:
                return False
        return True
        