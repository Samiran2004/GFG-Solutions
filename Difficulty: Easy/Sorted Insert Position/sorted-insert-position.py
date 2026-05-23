class Solution:
    def searchInsertK(self, arr, k):
        # code here
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] < k:
                left = mid + 1
            else:
                right = mid
        
        if arr[left] < k:
            return left + 1
        else:
            return left