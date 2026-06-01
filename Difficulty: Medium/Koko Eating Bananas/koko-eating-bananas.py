class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def check(arr, mid, k):
            totalHr = 0
            for i in range(len(arr)):
                totalHr += (arr[i] + mid - 1) // mid
            return totalHr <= k
        
        lo = 1
        hi = max(arr)
        res = hi
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if check(arr, mid, k) == True:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res