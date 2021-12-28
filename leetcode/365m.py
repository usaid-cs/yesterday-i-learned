"""
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

    Fill any of the jugs with water.
    Empty any of the jugs.
    Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
"""
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q = [(0, 0)]
        visited = set()
        
        while q:
            state = q.pop(0)
            if state in visited:
                continue
            visited.add(state)
            jug1, jug2 = state
            
            if targetCapacity in [jug1, jug2, jug1 + jug2]:
                return True
            # empty 1
            q.append((0, jug2))
            # empty 2
            q.append((jug1, 0))
            # fill 1
            q.append((jug1Capacity, jug2))
            # fill 2
            q.append((jug1, jug2Capacity))
            # pour 1 into 2
            max_accepted_2 = jug2Capacity - jug2
            if jug1 >= max_accepted_2:  # jug1 has leftover
                q.append((jug1 - max_accepted_2, jug2Capacity))
            else:
                q.append((0, jug2 + jug1))
            # pour 2 into 1
            max_accepted_1 = jug1Capacity - jug1
            if jug2 >= max_accepted_1:  # jug2 has leftover
                q.append((jug1Capacity, jug2 - max_accepted_1))
            else:
                q.append((jug2 + jug1, 0))
            
        return False



class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visited = set()

        def recurse(jug1, jug2):
            state = (jug1, jug2)
            if state in visited:
                return False
            visited.add(state)
            if targetCapacity in [jug1, jug2, jug1 + jug2]:
                return True

            # empty 1
            if recurse(0, jug2):
                return True
            # empty 2
            if recurse(jug1, 0):
                return True
            # fill 1
            if recurse(jug1Capacity, jug2):
                return True
            # fill 2
            if recurse(jug1, jug2Capacity):
                return True
            # pour 1 into 2
            max_accepted_2 = jug2Capacity - jug2
            if jug1 >= max_accepted_2:  # jug1 has leftover
                if recurse(jug1 - max_accepted_2, jug2Capacity):
                    return True
            else:
                if recurse(0, jug2 + jug1):
                    return True
            # pour 2 into 1
            max_accepted_1 = jug1Capacity - jug1
            if jug2 >= max_accepted_1:  # jug2 has leftover
                if recurse(jug1Capacity, jug2 - max_accepted_1):
                    return True
            else:
                if recurse(jug2 + jug1, 0):
                    return True

        return recurse(0, 0)
