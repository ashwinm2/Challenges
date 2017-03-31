class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = {}
        l = len(nums)
        i = 0
        if l < 1:
            return nums
        else:
            nums = sorted(nums)
            while i < l - 1:
                start, end = i+1, l - 1
                while start < end:
                    temp = nums[i] + nums[start] + nums[end]
                    if temp < 0:
                        start += 1
                    elif temp > 0:
                        end -= 1
                    else:
                        temp = nums[i]
                        const = (nums[i], nums[start], nums[end])
                        #print "The set", const
                        if const not in sol:
                            sol[const] = 0
                        if nums[start] == nums[end]:
                            start = end
                        else:
                            start += 1
                            end -= 1
                i += 1
        #print sol
        return sol.keys()
        