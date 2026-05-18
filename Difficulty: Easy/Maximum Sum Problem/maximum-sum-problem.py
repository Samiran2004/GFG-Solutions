class Solution:
    def maxSum(self, n):
        # code here
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            break_sum = dp[i // 2] + dp[i // 3] + dp[i // 4]
            dp[i] = max(break_sum, i)
        
        return dp[n]