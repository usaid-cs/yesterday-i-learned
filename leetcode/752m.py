class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = []
        dead_ends = set()
        visited = set()

        if "0000" in deadends:
            return -1

        q.append(("0000", 0))
        while q:
            current_combo, turns = q.pop(0)
            if current_combo == target:
                return turns
            if current_combo in visited:
                continue
            visited.add(current_combo)

            for digit_pos in range(4):
                if current_combo[digit_pos] == '9':
                    # increment with wrap around
                    new_combo = (
                        current_combo[:digit_pos] +
                        '0' +
                        current_combo[digit_pos + 1:])
                else:
                    # increment with no wrap around
                    new_combo = (
                        current_combo[:digit_pos] +
                        str(int(current_combo[digit_pos]) + 1) +
                        current_combo[digit_pos + 1:])
                if new_combo not in deadends and new_combo not in visited:
                    q.append((new_combo, turns + 1))

                if current_combo[digit_pos] == '0':
                    # decrement with wrap around
                    new_combo = (
                        current_combo[:digit_pos] +
                        '9' +
                        current_combo[digit_pos + 1:])
                else:
                    # decrement with no wrap around
                    new_combo = (
                        current_combo[:digit_pos] +
                        str(int(current_combo[digit_pos]) - 1) +
                        current_combo[digit_pos + 1:])
                if new_combo not in deadends and new_combo not in visited:
                    q.append((new_combo, turns + 1))
        return -1
