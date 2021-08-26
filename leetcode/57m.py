class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        overlap = newInterval
        for interval in intervals:
            start, end = interval

            # Cases that don't overlap
            if end < newInterval[0] or start > newInterval[1]:
                output.append(interval)
                continue

            overlap[0] = min(start, overlap[0])
            overlap[1] = max(end, overlap[1])

        print(output, overlap)
        output.append(overlap)
        output = [tuple(x) for x in output]
        output.sort(key=lambda x: x[0])
        output = [list(x) for x in output]
        return output
