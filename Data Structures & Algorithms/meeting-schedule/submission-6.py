"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Overlap if a[0] < b[0] < a[1] OR b[1] > a[0] and b[1] < a[1]

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key=lambda x: x.start)

        prev = intervals[0]
        for curr in intervals[1:]:
            if prev.end > curr.start:
                return False
            
            prev = curr

        return True