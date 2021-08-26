class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = []
        gate = 0

        for y, row in enumerate(rooms):
            for x, room in enumerate(row):
                if room >= 0:
                    q.append((y, x, room))

        while q:
            cell = q.pop(0)
            y, x, distance_from_gate = cell
            if y > 0:
                top_cell = rooms[y - 1][x]
                if top_cell > (distance_from_gate + 1):
                    rooms[y - 1][x] = distance_from_gate + 1
                    q.append((y - 1, x, distance_from_gate + 1))
            if y <= len(rooms) - 2:
                below_cell = rooms[y + 1][x]
                if below_cell > (distance_from_gate + 1):
                    rooms[y + 1][x] = distance_from_gate + 1
                    q.append((y + 1, x, distance_from_gate + 1))
            if x > 0:
                left_cell = rooms[y][x - 1]
                if left_cell > (distance_from_gate + 1):
                    rooms[y][x - 1] = distance_from_gate + 1
                    q.append((y, x - 1, distance_from_gate + 1))
            if x <= len(rooms[0]) - 2:
                right_cell = rooms[y][x + 1]
                if right_cell > (distance_from_gate + 1):
                    rooms[y][x + 1] = distance_from_gate + 1
                    q.append((y, x + 1, distance_from_gate + 1))
