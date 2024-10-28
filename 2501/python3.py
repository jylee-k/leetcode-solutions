class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        from math import sqrt
        numset = set(nums)
        ans = 0
        for i in nums:
            # check if it's the smallest in a square walk
            sqr = sqrt(i)
            if type(sqr) is int:
                if sqr in numset:
                    continue
            count = 0
            sq = i
            while sq in numset:
                count += 1
                sq *= sq
            ans = max(ans, count)

        return ans if ans > 1 else -1
