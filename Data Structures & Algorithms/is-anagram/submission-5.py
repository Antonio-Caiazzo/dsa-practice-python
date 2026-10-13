from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = {}, {}
        for c in s:
            if c in counter_s:
                counter_s[c] += 1
            else:
                counter_s[c] = 1


        for c in t:
            if c in counter_t:
                counter_t[c] += 1
            else:
                counter_t[c] = 1
        
        return counter_s == counter_t
        