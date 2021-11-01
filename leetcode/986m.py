class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_ptr = 0
        second_ptr = 0
        overlaps = []

        while first_ptr < len(firstList) and second_ptr < len(secondList):
            first = firstList[first_ptr]
            second = secondList[second_ptr]
            if first[0] < second[0]:
                if first[1] < second[0]:
                    # the two don't overlap
                    pass
                else:
                    overlaps.append([second[0], min(first[1], second[1])])
            elif second[0] <= first[0]:
                if second[1] < first[0]:
                    # the two don't overlap
                    pass
                else:
                    overlaps.append([first[0], min(first[1], second[1])])
            if first[1] < second[1]:
                first_ptr += 1
            else:
                second_ptr += 1
        return overlaps