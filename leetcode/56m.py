class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        new_intervals = []
        idx = 0
        while idx < len(intervals) - 1:
            interval = intervals[idx]
            next_interval = intervals[idx + 1]
            if interval[0] <= next_interval[0] <= interval[1]:
                intervals[idx] = [interval[0],
                                  max(next_interval[1], interval[1])]
                intervals.pop(idx + 1)
            else:
                idx += 1
        return intervals
