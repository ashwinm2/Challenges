# Permutation without duplicates
class Solution(object):
    def calc(self, nums):
        l = len(nums)
        if l == 2:
            if nums[0] == nums[1]:
                return [nums]
            else:
                return [nums, [nums[1], nums[0]]]
        else:
            tp = []
            hashmap = {}
            for ele in range(l):
                each = nums[ele]
                if each not in hashmap:
                    hashmap[each] = 0
                    each = nums[ele]
                    part = nums[:ele] + nums[ele + 1:]
                    combi = self.calc(part)
                    for unit in combi:
                        tp.append([each] + unit)
            return tp
            
    def permuteUnique(self, nums):
        if len(nums) == 0:
            total = []
        elif len(nums) == 1:
            total = [nums]
        else:
            total = self.calc(nums)
        # for unit in self.compute(nums):
        #     total.append(unit)
        # print total
        return total
        
        