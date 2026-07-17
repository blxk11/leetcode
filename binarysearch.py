from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        s = []
        for i in nums:
            if i != c:
                s.append(i)
        zeros_needed = len(nums) - len(s)
        s = s + [0] * zeros_needed
        for j in range(len(nums)):
            nums[j] = s[j]