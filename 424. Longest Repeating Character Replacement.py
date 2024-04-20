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
        