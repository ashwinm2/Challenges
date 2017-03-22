# Product of Arrya except self
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        full_lt = nums
        total = 1
        output = []
        for i in full_lt:
            temp = total * 1
            total *= i
            output.append(temp)
        total = 1
        len_lt = len(full_lt) - 1
        for i in range(0, len_lt + 1):
            temp = total * 1
            total *= full_lt[len_lt - i]
            output[len_lt - i] = output[len_lt - i] * temp 
            
        return output