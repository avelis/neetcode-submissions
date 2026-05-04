"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            print(i)
            a = intervals[i]
            b = intervals[i + 1]
            if b.start < a.end:
                return False
        return True
