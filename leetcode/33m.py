from typing import List


def _assert(result, expected, notes=''):
    if result != expected:
        print('%s: expected result to be %s, got %s' % (notes, expected, result))


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print('-----')
        if nums[0] < nums[-1]:  # array is perfectly sorted
            pivot = 0
            new_nums = nums
        else:
            def find_pivot(idx_min, idx_max):
                if idx_max - idx_min == 0:
                    return idx_min
                elif idx_max - idx_min == 1:
                    if nums[idx_max] > nums[idx_min]:
                        return idx_min
                    return idx_max
                center = (idx_min + idx_max + 1) // 2
                # print(idx_min, center, idx_max)
                a, b, c = nums[idx_min], nums[center], nums[idx_max]
                # print(a, b, c)
                if a < b:  # Left section in correct order so go down the right
                    return find_pivot(center, idx_max)
                else:
                    return find_pivot(idx_min, center)

            pivot = find_pivot(0, len(nums) - 1)
            # print(pivot)
            new_nums = nums[pivot:] + nums[:pivot]

        # print(new_nums)

        def get_num_idx(idx_min, idx_max):
            if idx_max - idx_min == 0:
                if new_nums[idx_min] == target:
                    return (idx_min + pivot) % len(nums)
                return -1
            elif (idx_max - idx_min) == 1:
                num_here = new_nums[idx_min]
                if num_here == target:
                    return (idx_min + pivot) % len(nums)
                num_here = new_nums[idx_max]
                if num_here == target:
                    return (idx_max + pivot) % len(nums)
                return -1
            center = (idx_min + idx_max + 1) // 2
            num_at_center = new_nums[center]
            if target == num_at_center:
                return (center + pivot) % len(nums)
            elif target < num_at_center:
                return get_num_idx(idx_min, center - 1)
            elif target > num_at_center:
                return get_num_idx(center + 1, idx_max)
        return get_num_idx(0, len(nums) - 1)


a = Solution()
_assert(a.search([4,5,6,7,0,1,2], 0), 4, 'oh no 1')
_assert(a.search([4,5,6,7,0,1,2], 3), -1, 'oh no 2')
_assert(a.search([0], 0), 0, 'oh no 3')
_assert(a.search([1], 0), -1, 'oh no 4')
_assert(a.search([1, 3], 3), 1, 'oh no 5')
_assert(a.search([1, 3, 5], 1), 0, 'oh no 6')
_assert(a.search([5,1,2,3,4], 4), 4, 'oh no 7')
_assert(a.search([3, 5, 1], 3), 0, 'oh no 8')
