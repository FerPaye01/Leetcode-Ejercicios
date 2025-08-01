class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(n: int, first: int, last: int) -> int:
            steps = 0
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps

        curr = 1
        k -= 1 
        while k > 0:
            steps = countSteps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr


if __name__ == '__main__':
    test_cases = [
        (5, 2),  
        (3, 3),  
        (13, 2),  
        (13, 6),  
    ]

    sol = Solution()
    for n, k in test_cases:
        result = sol.findKthNumber(n, k)
        print(f"findKthNumber(n={n}, k={k}) = {result}")
"""Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 """