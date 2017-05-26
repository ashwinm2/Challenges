# Maximum subarray
class Solution(object):
    def maxSubArray(self, nums):
        index = 0
        length = len(nums)
        large = - sys.maxint - 1
        tot = 0
        while index < length:
            tot += nums[index]
            if tot > large:
                large = tot
            if tot < 0:
                tot = 0
            
            index += 1
        return large