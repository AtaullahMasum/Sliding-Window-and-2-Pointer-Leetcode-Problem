# Time Complexity is O(2*k)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum , maxSum = 0, 0, 0
        for i in range(k):
            lsum += cardPoints[i]
        maxSum = lsum
        rindex = len(cardPoints)-1
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum  += cardPoints[rindex]
            rindex -= 1
            maxSum = max(maxSum, lsum+rsum)
        return maxSum
        