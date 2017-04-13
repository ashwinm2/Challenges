# Reversing a number

class Solution(object):
    def reverse(self, x):
        if x < 0:
            flag = -1
            x = x * -1
        else:
            flag = 1
            
        rev = 0
        while x:
            temp = x % 10
            rev = temp + rev * 10
            x = x / 10
            
        if rev > 2147483647:
            return 0
        
        return rev * flag
            
        