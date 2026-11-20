from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        max_len = 0
        
        for num, count in freq.items():
            if num + 1 in freq:
                max_len = max(max_len, count + freq[num + 1])
                
        return max_len 