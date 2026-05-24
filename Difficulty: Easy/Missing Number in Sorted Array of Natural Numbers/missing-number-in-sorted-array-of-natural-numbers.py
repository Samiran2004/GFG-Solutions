class Solution:
    def missingNumber(self, arr):
        # code here
        
    
        n = len(arr) + 1
        
        totalSum = n * (n + 1) // 2
        arraySum = sum(arr)
        missingNum = totalSum - arraySum
        
        return missingNum