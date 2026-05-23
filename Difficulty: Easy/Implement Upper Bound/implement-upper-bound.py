import bisect

class Solution:
    def upperBound(self, arr, target):
        # code here
        return bisect.bisect_right(arr, target)