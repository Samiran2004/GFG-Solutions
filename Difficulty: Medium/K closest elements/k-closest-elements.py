class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        
        arr.sort(key=lambda a: (abs(a - x), -a))
        
        result = []
        count = 0
        
        for num in arr:
            if num == x:
                continue
            result.append(num)
            count += 1
            
            if count == k:
                break
        
        return result