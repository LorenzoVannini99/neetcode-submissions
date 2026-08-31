"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Idea:
Sort the intervals such that : [[start_1,end_1],[start_2,end_2],...] (start_i < end_i) with start_i <= start_i+1 and so on.

It's better to picture the problem.

A conflict arises if start_i+1 < end_i.

# Visualize:

[---- interval i ----]
          [---- interval i+1 ----]

A conflict occurs when interval i+1 starts before
interval i ends:

    start_(i+1) < end_i


If this happens, both meetings occupy part of the
same time range, so they overlap.

"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x : x.start)

        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        
        return True

