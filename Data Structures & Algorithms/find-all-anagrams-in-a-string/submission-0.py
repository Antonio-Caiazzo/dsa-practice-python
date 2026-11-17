from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
            
        frequency_p = Counter(p)
        frequency_s = {}
        result = []
        l = 0

        for c in range(len(p)):
            frequency_s[s[c]] = frequency_s.get(s[c], 0) + 1 

        if frequency_s == frequency_p:
            result.append(l)

        for r in range(len(p), len(s)):

            frequency_s[s[r]] = frequency_s.get(s[r], 0) + 1
            frequency_s[s[l]] -= 1
            if frequency_s[s[l]] == 0:
                del frequency_s[s[l]]
            l += 1

            if frequency_s == frequency_p:
                result.append(l)


        return result 
