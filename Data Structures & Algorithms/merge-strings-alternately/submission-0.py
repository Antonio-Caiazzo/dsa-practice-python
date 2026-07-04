class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = l2 =  0
        r1, r2 = len(word1), len(word2)

        result = []
        while l1 < r1 and l2 < r2:
            result.append(word1[l1])
            result.append(word2[l2])
            l1 += 1
            l2 += 1

        if l1 == r1:
            result.append(word2[l2:])
        elif l2 == r2:
            result.append(word1[l1:])

        return "".join(result)

        