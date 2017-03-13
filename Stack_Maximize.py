# Stock Maximize
import sys

def compute(prices, total):
    max_v = 0
    max_p = 0
    temp = []
    sum_l = 0
    prev = 0
    for i in range(0, len(prices)):
        sum_l += prev
        prev = prices[i]
        temp.append(sum_l)
        if max_v < prices[i]:
            max_v = prices[i]
            max_p = i
    
    #print "List", temp
    total += (max_p * max_v) - temp[max_p]
    #print "Values", total, max_p, max_v
    if len(prices[max_p:]) > 1:
        #print "Times"
        total += compute(prices[max_p+1:], 0)
    return total
    
    
t = int(raw_input().strip())
for a0 in xrange(t):
    N = int(raw_input().strip())
    prices = map(int, raw_input().strip().split(' '))
    total = compute(prices, 0)
    print total