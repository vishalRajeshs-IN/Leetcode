from collections import Counter
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        freq = Counter(f for f, _ in items)
        max_f = max(freq)
        divisible_count = [0] * (max_f + 1)
        
        for f in freq:
            for multiple in range(f, max_f + 1, f):
                divisible_count[f] += freq[multiple]

        dp = [0] * (budget + 1)
        min_price = budget + 1

        for f, p in items:
            if p < min_price:
                min_price = p
            val = divisible_count[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + val > dp[b]:
                    dp[b] = dp[b - p] + val

        ans = 0
        for b in range(budget + 1):
            extra = (budget - b) // min_price if min_price <= budget else 0
            if dp[b] + extra > ans:
                ans = dp[b] + extra

        return ans        