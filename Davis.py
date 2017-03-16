# Davi's Staircase
def compute(n, dict_l):
    if n in dict_l.keys():
        return dict_l[n]
    
    if n-1 not in dict_l.keys():
        val = compute(n-1, dict_l)
        #print 'Val computed for', n-1, val
        dict_l[n-1] = val
    else:    
        return dict_l[n-1] + dict_l[n-2] + dict_l[n-3]
    return dict_l[n-1] + dict_l[n-2] + dict_l[n-3]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    dict_l = {3:4,2:2,1:1,0:0}
    p = compute(n,dict_l)
    #print p,q,r
    print p