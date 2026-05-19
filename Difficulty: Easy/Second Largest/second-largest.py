class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        arr.sort()
        
        maximum = arr[-1]
        
        for i in range(n - 2, -1, -1):
            if arr[i] != maximum:
                return arr[i]
        return -1