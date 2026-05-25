class Solution:
    def search(self, arr, key):
        # code here
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == key:
                return mid
            
            if arr[low] <= arr[mid]:
                if key >= arr[low] and key <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if key >= arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1