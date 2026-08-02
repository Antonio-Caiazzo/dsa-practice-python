class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        total = sum(arr[:k])        
        l = 0
        result = 1 if total / k >= threshold else 0

        for r in range(k, len(arr)):
            
            total += arr[r]
            
            total -= arr[l]
            l += 1

            if total / k >= threshold:
                result += 1   
     
        return result



                     
        
        