class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        longest_substring = 0

        l = 0

        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring

        