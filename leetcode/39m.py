class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        candidates = sorted(candidates)
        def dfs(current_combo, running_total):
            for candidate in candidates:
                this_sum = sum(x for x in current_combo) + candidate
                if this_sum == target:
                    combo = sorted(current_combo + [candidate])
                    if combo not in combos:
                        combos.append(combo)
                elif this_sum > target:
                    continue
                else:
                    dfs(current_combo + [candidate], this_sum)
        dfs([], 0)
        return combos
