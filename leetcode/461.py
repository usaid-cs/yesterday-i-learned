class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = bin(x)[2:].zfill(32)
        ybin = bin(y)[2:].zfill(32)
        idxs = []
        for idx, (xi, yi) in enumerate(zip(xbin, ybin)):
            if xi != yi:
                idxs.append(idx)
        return len(idxs)


a = Solution()
assert a.hammingDistance(1, 4) == 2