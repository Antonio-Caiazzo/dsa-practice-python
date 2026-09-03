class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currComb, resultComb = [], []

        def dfs(i):
            
            if len(currComb) == k:
                resultComb.append(currComb.copy())
                return
            if i > n:
                return
            
            
            for j in range(i, n + 1):
                currComb.append(j)
                dfs(j + 1)
                currComb.pop()
        dfs(1)
        return resultComb

        