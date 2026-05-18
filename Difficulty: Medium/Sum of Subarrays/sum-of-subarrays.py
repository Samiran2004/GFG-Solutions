class Solution:
    def subarraySum(self, arr):
        # code here 
        # result = 0
        # n = len(arr)
        
        # for i in range(n):
        #     temp = 0
        #     for j in range(i, n):
        #         temp += arr[j]
        #         result += temp
        
        # return result
        
        result = 0
        n = len(arr)
        
        for i in range(n):
            result += arr[i] * (i + 1) * (n - i)
        
        return result