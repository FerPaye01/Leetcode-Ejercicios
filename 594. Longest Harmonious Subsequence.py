from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        best=0
        freq= Counter(nums)
        for i in freq:
            if i+1 in freq:
                dif=freq[i]+freq[i+1]
                if dif>best:
                    best=dif
        return best



def main():
    sol = Solution()

    test_cases = [
        ([1,3,2,2,5,2,3,7]),      # Esperado: 5
        ([1,2,3,4]),     # Esperado: 2
        ([1,1,1,1]),    # Esperado: 0
        ([1,2,2,3,4,5,1,1,1,1]), # Esperado: 7
        ([1,4,1,3,1,-14,1,-13])# Esperado: 2
    ]

    for i, (nums) in enumerate(test_cases):
        result = sol.findLHS(nums)
        print(f"Test case {i + 1}: nums = {nums} → Result = {result}")

if __name__ == "__main__":
    main()
