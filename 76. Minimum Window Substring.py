# Brute Force Approch
# Time Complexity O(n^2)
# Space Complexity is O(256)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen, sIndex = 10**9, -1  
        n, m = len(s), len(t)
        for i in range(n):
            hashMap = [0]*256
            cnt = 0
            for j in range(m):
                hashMap[ord(t[j]) ] += 1
            for j in range(i, n):  
                if hashMap[ord(s[j])]> 0:
                    cnt += 1
                hashMap[ord(s[j])]  -= 1
                if cnt == m:
                    if (j - i + 1) < minLen:
                        minLen = j - i + 1
                        sIndex = i
                        break
        if sIndex == -1:
            return ""
        else:
            return s[sIndex:sIndex+minLen]
