class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        odd_freqs = []
        even_freqs = []
        for f in freq:
            if f > 0:
                if f % 2 == 1:
                    odd_freqs.append(f)
                else:
                    even_freqs.append(f)

        return max(odd_freqs) - min(even_freqs)


if __name__ == '__main__':
    test_cases = [
        (5, 2), 
        (3, 3), 
    ]
    for odd_count, even_count in test_cases:
        result = odd_count - even_count
        print(result)
"""Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 """