# Chief Hopper
n = int(raw_input())
lt = map(int, raw_input().split(' '))
init = 0
cumulat = lt[0]
for i in range(0,len(lt)):
    if cumulat - lt[i] < 0:
        temp = cumulat
        temp_init = init
        print "outside", lt[i], cumulat, init
        while temp < lt[i]:
            temp_init += 1
            diff = temp_init - init
            eq = (i - 1)
            split = 2**eq
            split = 2 * diff * split
            temp = cumulat + split
            print "Inside", temp, "Temp_init", temp_init, "Val", temp_init + lt[0]   
        cumulat = temp + (temp - lt[i])
        init = temp_init
        print "Result", temp, "Cumulat", cumulat,"init", init, "Final Val", init+lt[0]
    else:
        cumulat += (cumulat - lt[i])
print init + lt[0]