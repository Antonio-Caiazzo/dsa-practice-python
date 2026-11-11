from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter_s1 = Counter(s1)
        counter_s2 = {}

        for i in range(len(s1)):
            counter_s2[s2[i]] = counter_s2.get(s2[i], 0) + 1

        if counter_s1 == counter_s2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            counter_s2[s2[r]] = counter_s2.get(s2[r], 0) + 1
            counter_s2[s2[l]] -= 1
            if counter_s2[s2[l]] == 0:
                del counter_s2[s2[l]]

            if counter_s1 == counter_s2:
                return True

            l += 1

        return False
