class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = list(str(x))
        i = 0
        if l[i] == '-' or l[i] == '+':
            return False
            
        ls = len(l) - 1
        while i <= ls and i < (ls - i):
            if l[i] == l[ls-i]:
                i += 1
            else:
                return False
                
        return True
        