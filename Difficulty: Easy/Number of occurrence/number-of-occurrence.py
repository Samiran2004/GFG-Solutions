import bisect

class Solution:
    def countFreq(self, arr, target):
        # code here
        
        r = bisect.bisect_right(arr, target)
        l = bisect.bisect_left(arr, target)
        
        return r - l
        