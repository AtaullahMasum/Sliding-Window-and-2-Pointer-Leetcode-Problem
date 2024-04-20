# Using Sliding Window and Two Pointer 
class Solution:
    def helper(self, nums, k):
        if k < 0:
            return 0
        l, r, preSum , cnt = 0,0,0,0
        while r < len(nums):
            preSum += nums[r]%2
            while preSum > k:
                preSum -= nums[l]%2
                l += 1
            cnt += (r - l + 1)
            r += 1
        return cnt
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k-1)
# Using Prefix sum and Hashing
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashMap = {0: 1}
        cnt = 0
        preSum = 0
        for num in nums:
            preSum += num%2
            cnt += hashMap.get(preSum - k, 0)
            hashMap[preSum] = hashMap.get(preSum, 0) + 1
        return cnt