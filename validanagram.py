from typing import list
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char  in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] = count[char] - 1
            else:
                count[char] = 1
        for val in count.values():
            if val != 0:
                return False
        return True
