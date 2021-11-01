# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            is_bad = isBadVersion(middle)
            if is_bad:
                if not isBadVersion(middle - 1):
                    return middle
                right = middle - 1
            else:
                left = middle + 1
