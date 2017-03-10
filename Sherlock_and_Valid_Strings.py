# Sherlock and Valid Strings
s = list(raw_input())
total = {}
for i in s:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1
#print total
key_index = {}
min_s = 0
count = 0
for key in total:
    if total[key] not in key_index:
        key_index[total[key]] = 1
        count += 1
        if min_s == 0:
            min_s = total[key]
        else:
            if min_s  > total[key]:
                min_s = total[key]
    else:
        key_index[total[key]] += 1
#print key_index
#print count, "Min", min_s

if count == 1:
    print "YES"
elif count > 2:
    print "NO"
else:
    if key_index[min_s] > 1:
        if (min_s + 1) not in key_index:
            print "NO"
        else:
            if key_index[min_s + 1] > 1:
                print "NO"
            else:
                print "YES"
    else:
        print "YES"