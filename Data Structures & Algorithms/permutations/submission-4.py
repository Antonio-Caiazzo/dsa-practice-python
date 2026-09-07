class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            new_perm = []
            for p in result:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    new_perm.append(pCopy)
            result = new_perm
        return result