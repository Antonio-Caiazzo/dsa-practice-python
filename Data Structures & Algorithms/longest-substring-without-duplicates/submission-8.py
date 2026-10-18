class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while l <= r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longestSubstring = max(longestSubstring, r - l + 1)

        return longestSubstring