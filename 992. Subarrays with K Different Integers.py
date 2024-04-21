# Brute Force Solution 
# Time Complexity is O(n^2)
# Space Complexity is O(n)
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        cnt = 0
        for i in range(len(nums)):
            hashMap = {}
            for j in range(i, len(nums)):
                hashMap[nums[j]] = hashMap.get(nums[j], 0) + 1
                if len(hashMap) == k:
                    cnt += 1
                elif len(hashMap) > k:
                    break
        return cnt
        
# Optimal Solution
# Time Complexity is O(4*n)
# Space Complexity is O(n)
class Solution:
    def countSubarryAtMostK(self, nums, k):
        l, r, cnt = 0, 0, 0
        hashMap = {}
        while r < len(nums):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
            else:
                hashMap[nums[r]] = 1
            while len(hashMap) > k:
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                l += 1
            cnt += (r -l + 1)
            r += 1
        return cnt
    def subarraysWithKDistinct(self, nums, k):
        return self.countSubarryAtMostK(nums, k) - self.countSubarryAtMostK(nums, k-1)
        