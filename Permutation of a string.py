# Permutation of a string
class Solution(object):
    def compute(self, nums):
        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [nums]
        else:
            tp = []
            for ele in range(len(nums)):
                each = nums[ele]
                remain = nums[:ele] + nums[ele + 1:]
                for part in self.compute(remain):
                    tp.append([each] + part)
            return tp


    def permute(self, nums):
        total = []
        for unit in self.compute(nums):
            total.append(unit)
        return total