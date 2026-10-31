class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        result = [[intervals[0][0], intervals[0][1]]]

        for start, end in intervals[1:]:
            
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])



        return result
        