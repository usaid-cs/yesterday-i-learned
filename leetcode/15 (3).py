class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     triplets = []
    #     for idx, i in enumerate(nums):
    #         for idx2, j in enumerate(nums):
    #             for idx3, k in enumerate(nums):
    #                 if idx != idx2 and idx2 != idx3 and idx != idx3:
    #                     if i + j + k == 0:
    #                         triplets.append(i, j, k)
    #     return triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(idx, n):
            twosum_cache = {}
            target = -n
            for idx2, num in enumerate(nums):
                if num in twosum_cache:
                    twosum_cache[num].append(idx2)
                else:
                    twosum_cache[num] = [idx2]

            solutions = []
            done_onesum_on = set()
            for idx2, num in enumerate(nums):
                if idx == idx2:
                    continue
                if (target - num) in done_onesum_on:
                    continue
                if (target - num) in twosum_cache:
                    for idx3 in twosum_cache[target - num]:
                        if idx3 not in (idx, idx2):
                            solutions.append([n, num, target - num])
                done_onesum_on.add(target - num)
            return solutions

        nums.sort()
        done_twosum_on = set()
        solutions = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if num in done_twosum_on:
                continue
            solutions.extend(twosum(idx, num))
            done_twosum_on.add(num)

        solutions = [sorted(x) for x in solutions]
        solutions = [tuple(x) for x in solutions]
        solutions = list(set(solutions))
        return solutions
