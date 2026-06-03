#User function Template for python3

class Solution:
	def minDiff(self, arr):
		# Code here
# 		minDiff = float('inf')
		
# 		for i in range(len(arr) - 1):
# 		    for j in range(i + 1, len(arr)):
# 		        if abs(arr[i] - arr[j]) < minDiff:
# 		            minDiff = abs(arr[i] - arr[j])
		
# 		return minDiff

        arr.sort()
        n = len(arr)
        diff = float('inf')
        
        for i in range(n - 1):
            if arr[i + 1] - arr[i] < diff:
                diff = arr[i + 1] - arr[i]
        
        return diff