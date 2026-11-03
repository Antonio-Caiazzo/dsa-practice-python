"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
            
        result = 1
        intervals.sort(key=lambda x: x.start)
        minEnd = [intervals[0].end]

        for interval in intervals[1::]:

            start = interval.start
            end = interval.end

            if start >= minEnd[0]:
                heapq.heappop(minEnd)
                
            else:
                result += 1
            heapq.heappush(minEnd, end)
        return result


        