class Solution:
    def countIncreasing(self, arr):
        # code here.
        n = len(arr)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j - 1] >= arr[j]:
                    break
                count += 1
        return count