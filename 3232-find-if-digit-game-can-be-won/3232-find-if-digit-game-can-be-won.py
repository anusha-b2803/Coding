class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(v for v in nums if v < 10) != sum(v for v in nums if v > 9)