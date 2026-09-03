"""
Idea :

Sort the meetings by their start time.

We use a min-heap to store the end time of each meeting
currently occupying a room.

The minimum value in the heap represents the earliest
time at which a room becomes available.

For each new meeting:

If start >= min_heap[0]:
    A room is available, so we can reuse it.
    Remove the earliest end time from the heap.

Otherwise:
    All existing rooms are still occupied, so we need
    a new room.

In both cases, add the new meeting's end time to the heap.

The maximum number of rooms required is the maximum size
of the heap.

"""
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        rooms = 1

        for i in range(1, len(intervals)):

            start = intervals[i].start
            end = intervals[i].end

            if start >= min_heap[0]:
                # A room is free → reuse it
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, end)

            else:
                # Every room is occupied → need a new room
                rooms += 1
                heapq.heappush(min_heap, end)

            

        return rooms
        