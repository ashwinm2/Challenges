# Journey to Moon
N,l = map(int,raw_input().split())

full_map = {}
count = 0
total = 0
for i in xrange(l):
    flag = 0
    conjoint_lt = []
    a,b = map(int,raw_input().split())
    for key in full_map.keys():
        temp = full_map[key]
        if a in temp and b in temp:
            flag = 1
        elif a in temp or b in temp:   
            conjoint_lt.append(key)
            flag = 2
    #print a, b
    #print flag
    if flag == 0:
        full_map[count] = {a:a, b:b}
        count += 1
        total += 2
    elif flag == 2:
        key = conjoint_lt[0]
        temp = full_map[key]
        #print conjoint_lt
        if len(conjoint_lt) > 1:
            for each in conjoint_lt:
                temp.update(full_map[each]) 
                del full_map[each]
        if a not in temp:
            temp[a] = a
            total += 1
        elif b not in temp:
            temp[b] = b
            total += 1
        full_map[key] = temp
        #print full_map
#print "------------------------"
#print full_map
#print total
reminder = (N - total)
result = reminder * total
reminder = reminder * (reminder - 1)/2
result += reminder
for key in full_map:
    temp_l = len(full_map[key].keys())
    total = total - temp_l
    result += temp_l * total
#print "------------------------"
print result
