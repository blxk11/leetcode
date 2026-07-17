from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for i in nums:
            n.append(i * i)
            n.sort()
            
        