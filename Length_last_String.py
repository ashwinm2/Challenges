# Length of last String
class Solution(object):
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        else:
            l = s.split(" ")
            count = -1
            while l[count] == "" and count + len(s) >= 0:
                count -= 1
            if count + len(s) >= 0:    
                return len(l[count])
            else:
                return 0