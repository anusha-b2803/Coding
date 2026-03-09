class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k] - int(i > k), t) for i, t in enumerate(tickets))