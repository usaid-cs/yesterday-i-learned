class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def get_buildings_at_x(x):
            output = []
            for building in buildings:
                x1, x2, y = building
                if x1 <= x < x2:
                    output.append(building)
            return output

        def get_max_height_at_x(x):
            buildings_at_x = get_buildings_at_x(x)
            if not buildings_at_x:
                return 0
            return max(lol[2] for lol in buildings_at_x)

        output = []
        x_max = max(lol[1] for lol in buildings)
        prev_y = 0
        for x in range(x_max):
            y = get_max_height_at_x(x)
            if y != prev_y:
                output.append([x, y])
                prev_y = y
        output.append([x_max, 0])  # Last building ends
        return output
