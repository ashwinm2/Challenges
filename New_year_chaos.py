# New Year Chaos
import sys

def swap(q, index):
    count = 0
    #print index
    while index != 0:
        if q[index] < q[index - 1]:
            temp = q[index - 1]
            q[index - 1] = q[index]            
            q[index] = temp
            count += 1 
        else:
            index = 1
        index = index - 1
    #print q, count
    return q, count
    
def calc(q):
    total = 0
    #print "New List", q
    for index in range(0, len(q)):
        index_val = q[index]
        act_val = index + 1
        if index_val - act_val > 2:
            print "Too chaotic"
            return -1
        else:
            q, count = swap(q, index)
            total += count
    return total

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    total = 0
    result = calc(q)
    if result != -1:
        print result
                
                    
             
        
    
    
