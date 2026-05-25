class Solution:
    def search(self, arr, key):
        # code here
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == key:
                return True
            
            if arr[left] == arr[mid] and arr[right] == arr[mid]:
                left += 1
                right -= 1
                continue
            
            if arr[left] <= arr[mid]:
                if arr[left] <= key and arr[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] < key and arr[right] >= key:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
        