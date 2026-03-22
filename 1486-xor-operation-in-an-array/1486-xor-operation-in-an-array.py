class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_sum = 0
        for i in range(n):
            xor_sum ^= (start + 2 * i)
        return xor_sum