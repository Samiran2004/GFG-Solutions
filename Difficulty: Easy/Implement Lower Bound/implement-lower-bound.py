import bisect

class Solution:
    def lowerBound(self, arr, target):
        # code here
        return bisect.bisect_left(arr, target)