class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(m: int) -> int:
            return (m * (m - 1) // 2) if m >= 2 else 0
            
        total = comb2(n + 2)
        total -= 3 * comb2(n - limit + 1)
        total += 3 * comb2(n - 2 * limit)
        total -= comb2(n - 3 * limit - 1)     
            
        return total


if __name__ == "__main__":
    test_cases = [
        (5, 2),
        (3, 3),
    ]
    sol = Solution()
    for n, limit in test_cases:
        result = sol.distributeCandies(n, limit)
        print(f"n = {n}, limit = {limit} -> {result}")
