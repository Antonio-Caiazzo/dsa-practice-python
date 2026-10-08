class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(len(intervals)):
            last = result[-1]
            current = intervals[i]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                result.append(current)
            
        return result



        