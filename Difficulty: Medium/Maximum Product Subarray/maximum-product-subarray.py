class Solution:
	def maxProduct(self,arr):
		# code here
# 		maxProd = arr[0]
# 		n = len(arr)
		
# 		for i in range(n):
# 		    mul = 1
# 		    for j in range(i, n):
# 		        mul *= arr[j]
# 		        maxProd = max(maxProd, mul)
		
# 		return maxProd

        currMax = arr[0]
        currMin = arr[0]
        maxProd = arr[0]
        n = len(arr)
        
        for i in range(1, n):
            temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)
            currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)
            currMax = temp
            maxProd = max(maxProd, currMax)
        
        return maxProd