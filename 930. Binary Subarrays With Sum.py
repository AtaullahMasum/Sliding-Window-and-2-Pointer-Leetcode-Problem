# Time Complexity is 2(O(n)+O(n)) = O(2x2n)
# Space Complexity is O(1)
class Solution:
    def helper(self, nums, goal):
        if goal < 0:
            return 0
        l, r, preSum , cnt = 0,0,0,0
        while r < len(nums):
            preSum += nums[r]
            while preSum > goal:
                preSum -= nums[l]
                l += 1
            cnt += (r - l + 1)
            r += 1
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.helper(nums, goal) - self.helper(nums, goal-1)