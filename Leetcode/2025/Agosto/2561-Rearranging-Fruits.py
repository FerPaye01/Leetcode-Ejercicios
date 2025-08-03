from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for x in basket1:
            cnt[x] += 1
        for x in basket2:
            cnt[x] -= 1
        
        min_val = min(min(basket1), min(basket2))
        swaps = []
        for k, v in cnt.items():
            if v % 2 != 0:
                return -1
            swaps.extend([k] * (abs(v) // 2))
        
        swaps.sort()
        k = len(swaps) // 2
        return sum(min(swaps[i], 2 * min_val) for i in range(k))

def main():
    sol = Solution()

    test_cases = [
        ([4,2,2,2], [1,4,1,2], 1),
        ([2,3,4,1], [3,2,5,1], -1),
        ([4,4,4,4], [2,2,2,2], 4),
        ([1,2,2,3], [1,3,3,3], 2),
        ([1,3,3], [2,2,1], 2)]

    for i, (b1, b2, expected) in enumerate(test_cases):
        result = sol.minCost(b1, b2)
        print(f"Test case {i + 1}: Result = {result} (Expected: {expected}) {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    main()