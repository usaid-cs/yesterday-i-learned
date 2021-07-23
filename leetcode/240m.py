class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix and matrix[0]:
            return False

        def is_found_in(x_min, y_min, x_max, y_max, last_x=None, last_y=None):
            x_mid = (x_min + x_max) // 2
            y_mid = (y_min + y_max) // 2
            #       0      0      0      3      4      3
            # print(x_min, x_max, x_mid, y_min, y_max, y_mid)
            if last_x == x_mid and last_y == y_mid:
                # We already did this once
                return False

            # print(x_min, x_max, x_mid, y_min, y_max, y_mid)

            # Look at the cross
            for y in range(y_min, y_max + 1):
                if matrix[y][x_mid] == target:
                    return True
            for x in range(x_min, x_max + 1):
                if matrix[y_mid][x] == target:
                    return True
            if x_min == x_max and y_min == y_max:
                # Nothing left to look at lol
                return False

            if matrix[y_mid][x_mid] < target:
                # The target is larger than the current number.
                # Discard top left
                # (i.e. look at bottom left, top right, and bottom right).
                return (
                    is_found_in(
                        x_min=x_min,
                        x_max=x_mid - 1,
                        y_min=y_mid + 1,
                        y_max=y_max,
                        last_x=x_mid,
                        last_y=y_mid) or
                    is_found_in(
                        x_min=x_mid + 1,
                        x_max=x_max,
                        y_min=y_min,
                        y_max=y_mid - 1,
                        last_x=x_mid,
                        last_y=y_mid) or
                    is_found_in(
                        x_min=x_mid + 1,
                        x_max=x_max,
                        y_min=y_mid + 1,
                        y_max=y_max,
                        last_x=x_mid,
                        last_y=y_mid)
                )
            if matrix[y_mid][x_mid] >= target:
                # The target is smaller than the current number.
                # Discard bottom right
                # (i.e. look at just top left, top right, bottom left).
                return (
                    is_found_in(
                        x_min=x_min,
                        x_max=x_mid - 1,
                        y_min=y_min,
                        y_max=y_mid - 1,
                        last_x=x_mid,
                        last_y=y_mid) or
                    is_found_in(
                        x_min=x_mid + 1,
                        x_max=x_max,
                        y_min=y_min,
                        y_max=y_mid - 1,
                        last_x=x_mid,
                        last_y=y_mid) or
                    is_found_in(
                        x_min=x_min,
                        x_max=x_mid - 1,
                        y_min=y_mid + 1,
                        y_max=y_max,
                        last_x=x_mid,
                        last_y=y_mid)
                )

        return is_found_in(x_min=0,
                           x_max=len(matrix[0]) - 1,
                           y_min=0,
                           y_max=len(matrix) - 1)
