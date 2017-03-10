# Candies

def recalc(i, curr, curr_cand, dic):
    tot = 0
    if dic[i][0] > curr:
        if curr_cand >= dic[i][1]:
            tot += curr_cand - dic[i][1] + 1
            dic[i][1] = curr_cand + 1
            if i - 1 >= 0:
                dic, temp = recalc(i-1, dic[i][0], dic[i][1], dic)
                tot += temp
    return dic, tot

n = int(raw_input())
tot = 0
dic = {}
for i in xrange(n):
    curr = int(raw_input())
    curr_cand = 1
    if dic != {}:
        if curr > prev:
            if curr_cand <= prev_cand:
                curr_cand = prev_cand + 1
        elif curr < prev:
            if curr_cand >= dic[i-1][1]:
                dic, temp = recalc(i-1, curr, curr_cand, dic)
                tot += temp
    dic[i] = [curr, curr_cand]
    prev = curr
    prev_cand = curr_cand
    tot += curr_cand

#print 'total', dic
print tot
        