class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sol = {}
        l = len(nums)
        i = 0
        closest = None
        closest_curr = None
        if l < 1:
            return nums
        else:
            nums = sorted(nums)
            print nums
            while i < l - 1:
                start, end = i+1, l - 1
                while start < end:
                    #print "Sets", nums[i], nums[start], nums[end]
                    temp = nums[i] + nums[start] + nums[end]
                    curr = abs(target - temp)
                    
                    if temp < target:
                        start += 1
                    elif temp > target:
                        end -= 1
                    else:
                        start = end
                        
                    if closest == None:
                        closest = temp
                        closest_curr = curr
                    elif closest_curr > curr:
                        closest = temp
                        closest_curr = curr
                    
                    #print "Current", temp, curr
                    #print "Computed", closest, closest_curr
                    #if nums[start] == nums[end]:
                    #    start = end
                    
                i += 1
        #print sol
        return closest