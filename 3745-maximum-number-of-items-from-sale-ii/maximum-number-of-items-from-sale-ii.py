from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        
        # Count occurrences of each factor
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
            
        # Precompute total items whose factor is a multiple of x
        multiples_count = [0] * (max_f + 1)
        for x in range(1, max_f + 1):
            if freq[x] > 0:
                for m in range(x, max_f + 1, x):
                    multiples_count[x] += freq[m]
                    
        # Sort items by price ascending
        sorted_items = sorted(items, key=lambda x: x[1])
        
        total_copies = 0
        min_price = sorted_items[0][1]
        
        # Only buy value-2 pairs if p < 2 * min_price (effective cost p/2 < min_price)
        for f, p in sorted_items:
            if p >= 2 * min_price:
                break
                
            gain = multiples_count[f] - 1  # Exclude self (i != j)
            if gain <= 0:
                continue
                
            can_buy = min(gain, budget // p)
            total_copies += can_buy * 2
            budget -= can_buy * p
                
        # Spend remaining budget on the single cheapest item
        total_copies += budget // min_price
        
        return total_copies