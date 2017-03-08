# Find max Xor value between the range
def  maxXor( l,  r):
    max_v = 0
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if max_v < (i ^ j):
                max_v = i ^ j
    #print max_v
    return max_v

_l = int(raw_input());

_r = int(raw_input());

res = maxXor(_l, _r);
print(res)