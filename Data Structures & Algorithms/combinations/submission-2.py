class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        currComb = []

        def combination(start):
            if len(currComb) == k:
                result.append(currComb.copy())
                return
            for i in range(start, n + 1):
                currComb.append(i)
                combination(i + 1)
                currComb.pop()
        
        combination(1)
        return result
        