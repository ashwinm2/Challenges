def f(x):
    return { 
            'M': 1000,
            'D': 500 ,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }[x]


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        total = 0
        i = 0
        while i < l:
            if s[i] == "I" or s[i] == "X" or s[i] == "C":
                temp = f(s[i])
                if i + 1 < l:
                    forw = f(s[i+1])
                    if temp < forw:
                        total += forw - temp
                        i += 1
                    else:
                        total += temp
                else:
                    total += temp
            else:
                total += f(s[i])
            #print "Check", s[i], total
            i += 1
        
        print total
        return total