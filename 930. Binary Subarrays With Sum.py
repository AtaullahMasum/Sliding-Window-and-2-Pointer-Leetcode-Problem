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
# Using PreFix sum
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = {0: 1}
        preSum = 0
        cnt = 0
        for num in nums:
            preSum += num
            if preSum - goal in hashMap:
                cnt += hashMap[preSum - goal]
            if preSum in hashMap:
                hashMap[preSum] += 1
            else:
                hashMap[preSum] = 1
        return cnt
         