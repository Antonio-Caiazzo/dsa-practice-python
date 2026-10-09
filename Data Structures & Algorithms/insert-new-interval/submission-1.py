class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, (start, end) in enumerate(intervals):
            if end < newInterval[0]:
                result.append([start, end])

            if start > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            if end >= newInterval[0]:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        
        result.append(newInterval)

        return result

