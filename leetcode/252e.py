"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        prev_end = None
        for start, end in intervals:
            if prev_end:
                if start < prev_end:
                    return False
            prev_end = end
        return True