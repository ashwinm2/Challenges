
class Solution(object):
    def compute(self, string):
        #print "Palindrome check", string
        start = 0
        end = len(string) - 1
        flag = end
        while string[start] == string[end] and start < end:
            start += 1
            end -= 1
        if start >= end:
            #print "True"
            return True
        #print "False"
        return False

    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        string = ""
        single = {}
        l = len(s)
        i = 0
        if l == 1:
            return s
        else:
            while i < l:
                if s[i] not in single:
                    single[s[i]] = [i]
                else:
                    temp = single[s[i]]
                    for j in temp:
                        if (i+1 - j) > length:
                            check = s[j:i+1]
                            #print check
                            if self.compute(check):
                                length = len(check)
                                string = check
                    single[s[i]].append(i)
                i += 1
                
        if string == "":
            string = s[0]
        return string
                
                
                
                