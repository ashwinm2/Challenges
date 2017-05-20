# Jump Game
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums) - 1
        if length == 0:
            return True
        else:
            index = length
            flag = 0
            jndex = -1
            while index >= 0:
                if jndex == -1 and nums[index] == 0:
                    jndex = index
                else:
                    if jndex != -1:
                        if jndex != length:
                            if nums[index] > jndex - index:
                                jndex = -1
                        else:
                            if nums[index] >= jndex - index:
                                jndex = -1
                index -= 1
            if jndex == -1:
                return True
            else:
                return False
                