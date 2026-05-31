import bisect

class Solution:
    def countXInRange(self, arr, queries):
        # code here
        # result = []
        
        # for query in queries:
        #     left, right, x = query
        #     count = 0
            
        #     for i in range(left, right + 1):
        #         if arr[i] == x:
        #             count += 1
            
        #     result.append(count)
        
        # return result
        
        result = []
        n = len(arr)
        
        for query in queries:
            l, r, x = query
            
            left = bisect.bisect_left(arr, x)
            
            if left == n or arr[left] != x:
                result.append(0)
                continue
            
            right = bisect.bisect_right(arr, x)
            
            right -= 1
            
            left = max(left, l)
            right = min(right, r)
            
            if left > right:
                result.append(0)
            else:
                result.append(right - left + 1)
        
        return result