# Time Complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxlen = 0, 0, 0
        n = len(s)
        hashMap = {}
        while r < n:
            if s[r] in hashMap:
                if hashMap[s[r]] >= l:
                    l = hashMap[s[r]] + 1
            length = r - l + 1
            maxlen = max(maxlen, length)
            hashMap[s[r]] = r
            r += 1
        return maxlen
        