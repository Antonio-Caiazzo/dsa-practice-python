class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_lenght = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_lenght = max(max_lenght, r - l + 1)

        return max_lenght

    