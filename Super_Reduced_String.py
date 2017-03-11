# Super Reduced String
s = list(raw_input())
i = 0
while i < len(s):
    if i + 1 < len(s):
        if s[i] == s[i+1]:
            #print i, s[i], s
            del s[i+1], s[i]
            #print s
            if i - 1 >= 0:
                i -= 1
        else:
            i += 1
    else:
        #print i, "Here", s
        i += 1
if s == []:
    print 'Empty String'
else:
    print "".join(s)