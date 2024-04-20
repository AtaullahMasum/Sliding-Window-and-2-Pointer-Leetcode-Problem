# Brute Force Approch
# Time Complexity is O(n^2)
# Space complexity is O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        for i in range(len(s)):
            hash, maxfreq = [0]*26, 0
            for j in range(i, len(s)):
                hash[ord(s[j]) - ord('A')] += 1
                maxfreq = max(maxfreq, hash[ord(s[j]) - ord('A')])
                changes = (j-i+1) - maxfreq
                if changes <= k:
                    maxlen = max(maxlen, (j-i+1))
                else:
                    break
        return maxlen
# Solution 2
# Time Complexity (O(n)+O(n))*26
# Space Complexity is O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen , l, r, maxfreq = 0, 0, 0, 0
        hashMap = [0]*26
        while r < len(s):
            hashMap[ord(s[r])-ord('A')] += 1
            maxfreq = max(maxfreq,  hashMap[ord(s[r])-ord('A')])
            while ((r - l + 1) - maxfreq) > k:
                hashMap[ord(s[l])- ord('A')] -= 1
                maxfreq = 0
                for i in range(26):
                    maxfreq = max(maxfreq, hashMap[i])
                l += 1
            if ((r-l+1) - maxfreq) <= k:
                maxlen = max(maxlen, (r-l+1))
            r += 1
        return maxlen  
# Solution 3
# Time Complexity O(n)+O(n)
# Space Complexity is O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen , l, r, maxfreq = 0, 0, 0, 0
        hashMap = [0]*26
        while r < len(s):
            hashMap[ord(s[r])-ord('A')] += 1
            maxfreq = max(maxfreq,  hashMap[ord(s[r])-ord('A')])
            while ((r - l + 1) - maxfreq) > k:
                hashMap[ord(s[l])- ord('A')] -= 1
                l += 1
            if ((r-l+1) - maxfreq) <= k:
                maxlen = max(maxlen, (r-l+1))
            r += 1
        return maxlen   
# Optimal Solution 
# Time Complexity is O(n)
# Space Complexity is O(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen , l, r, maxfreq = 0, 0, 0, 0
        hashMap = [0]*26
        while r < len(s):
            hashMap[ord(s[r])-ord('A')] += 1
            maxfreq = max(maxfreq,  hashMap[ord(s[r])-ord('A')])
            if ((r - l + 1) - maxfreq) > k:
                hashMap[ord(s[l])- ord('A')] -= 1
                l += 1
            if ((r-l+1) - maxfreq) <= k:
                maxlen = max(maxlen, (r-l+1))
            r += 1
        return maxlen
