from typing import list
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        reversed_s = s[::-1]
        return s == reversed_s 