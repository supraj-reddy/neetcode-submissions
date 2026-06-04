class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best, sumt, left = float('inf'), 0, 0
        for i, right in enumerate(nums):
            sumt += right
            if sumt >= target:
                while sumt >= target:
                    best = min(best, i - left + 1)
                    sumt -= nums[left]
                    left += 1
        if best == float('inf'):
            return 0
        else:
            return best
                    
            
