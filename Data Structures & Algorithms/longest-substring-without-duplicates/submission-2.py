class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set = set()
        l = 0
        maximum_length = 0

        for r in range(len(s)):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            maximum_length = max(maximum_length, r - l + 1)
            
        return maximum_length
        