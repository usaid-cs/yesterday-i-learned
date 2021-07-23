class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        going_up = True
        reversal_triggered = False
        prev = arr[0]
        for idx, x in enumerate(arr[1:], start=1):
            if x < prev:
                if idx == 1:
                    # Never went up
                    return False
                if going_up:
                    if not reversal_triggered:
                        reversal_triggered = True
                        going_up = False
            elif x > prev:
                if not going_up:
                    return False
            else:
                return False
            prev = x
        return going_up == False  # Ends up going down
