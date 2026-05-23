class Solution:
    def extractPoints(self, arr):
        # code here
        n = len(arr)
        result = []
        
        if n == 0:
            return result
        
        result.append(arr[0])
        
        for i in range(1, n - 1):
            
            if arr[i] > result[-1] and arr[i] > arr[i + 1]:
                result.append(arr[i])
            elif arr[i] < result[-1] and arr[i] < arr[i + 1]:
                result.append(arr[i])
        
        if arr[-1] != result[-1]:
            result.append(arr[-1])
        
        return result