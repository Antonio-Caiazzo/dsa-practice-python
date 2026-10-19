from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram = {}

        for word in strs:
            sorted_word = sorted(word)
            new_word = "".join(sorted_word)
            if new_word in anagram:
                anagram[new_word].append(word)
            else:
                anagram[new_word] = [word]

        return [x for x in anagram.values()]
