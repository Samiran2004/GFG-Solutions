class Solution:
    def single(self, arr):
        # code here
        
        n = len(arr)
        
        for i in range(0, n - 1, 2):
            if arr[i] != arr[i + 1]:
                return arr[i]
        
        return arr[n - 1]