import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(rate):
            return sum(math.ceil(pile/rate) for pile in piles)
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if hours_needed(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo