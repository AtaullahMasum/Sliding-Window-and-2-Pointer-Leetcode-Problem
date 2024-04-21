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
# optimal Solution 
# Time Complexity O(2n) + O(m)
# Space Complexity is O(256)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen, sIndex = 10**9, -1  
        n, m = len(s), len(t)
        l, r, cnt = 0, 0, 0
        hashMap = [0]*256
        for i in range(m):
            hashMap[ord(t[i])] += 1

        while r < n:
            if hashMap[ord(s[r])] > 0:
                cnt += 1
            hashMap[ord(s[r])] -= 1
            while cnt == m:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l
                hashMap[ord(s[l])] += 1
                if hashMap[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
            r += 1
        if sIndex == -1:
            return ""
        else:
            return s[sIndex: sIndex+minLen]
        
