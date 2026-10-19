from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram = {}

        for word in strs:
            sorted_word = sorted(word)
            if "".join(sorted_word) in anagram:
                anagram["".join(sorted_word)].append(word)
            else:
                anagram["".join(sorted_word)] = [word]

    
        return [x for x in anagram.values()]