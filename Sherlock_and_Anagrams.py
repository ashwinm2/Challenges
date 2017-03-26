# Sherlock and Anagrams
    
def compute(str_i):
    total = {}
    tot = 0
    for i in range(0,len(str_i)):
        for j in range(i,len(str_i)):
            temp = str_i[i:j+1]
            temp = ''.join(sorted(temp))
            if temp not in total:
                total[temp] = 1
            else:
                if total[temp] != 1:
                    tot += total[temp]
                else:
                    tot += 1
                #print temp, tot
                total[temp] = total[temp] + 1    
    #print total
    print tot
    
n = int(raw_input())
for i in xrange(n):
    compute(raw_input())