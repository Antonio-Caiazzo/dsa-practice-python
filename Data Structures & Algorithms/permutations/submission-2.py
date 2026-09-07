class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permutation(i):
            if i == len(nums):
                return [[]]

            currPerm = []
            newPerm = permutation(i + 1)
            for p in newPerm:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    currPerm.append(pCopy)
            return currPerm
        
        return permutation(0)
        