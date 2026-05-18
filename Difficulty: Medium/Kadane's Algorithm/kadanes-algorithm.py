class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        # res = 0
        # for i in range(len(arr)):
        #     currSum = 0
        #     for j in range(i, len(arr)):
        #         currSum += arr[j]
        #         res = max(res, currSum)
        
        # return res
        
        res = arr[0]
        maxEnding = arr[0]
        
        for i in range(1, len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            res = max(maxEnding, res)
        
        return res