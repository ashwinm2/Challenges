def f(x):
    return {
        '(': ')',
        '{': '}',
        '[': ']'
    }[x]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        final = []
        for ele in s:
            if ele == "(" or ele == "{" or ele == "[":
                final.append(ele)
            else:
                if final == []:
                    return False
                else:
                    temp = final.pop()
                    if ele != f(temp):
                        print "Check", ele
                        return False
                        
        if final != []:
            return False
        
        return True