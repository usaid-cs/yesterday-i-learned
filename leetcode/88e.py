class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            nums1.pop(-1)
            n -= 1
        print(nums1)
        num1_ptr = 0
        while nums2:
            num2_head = nums2[0]
            if num1_ptr >= len(nums1):
                break
            num1_val = nums1[num1_ptr]
            if num2_head > num1_val:
                # cannot insert yet
                num1_ptr += 1
                continue
            if num2_head <= num1_val:
                print('inserting', num1_ptr, num2_head)
                nums1.insert(num1_ptr, num2_head)
                nums2.pop(0)
            print(nums1)
        while nums2:
            nums1.append(nums2[0])
            nums2.pop(0)
