#  Find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        total = {}
        count = 0
        low = 0
        ele = 0
        t = s
        start = 0
        while ele < l:
            if s[ele] not in total:
                total[s[ele]] = ele
                low += 1
            else:
                #print "Break",total
                if low > count:
                    count = low
                el = total[s[ele]]
                r = t[start:el+1]
                start = el + 1
                #print "See", r
                for j in r:
                    del total[j]
                    low -= 1
                low += 1
                total[s[ele]] = ele
                #print "Reassign", total

                temp = ""
            ele += 1
        if low > count:
            count = low
        #print count
        return count