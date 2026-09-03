class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        currComb = []
        resultComb = []
    
        def dfs(i):
            if len(currComb) == k:
                resultComb.append(currComb.copy())
                return
            if i > n:
                return
            currComb.append(i)
            dfs(i + 1)
            currComb.pop()

            dfs(i + 1)

        dfs(1)
        return resultComb
