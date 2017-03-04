# Algorithmic Crush
n, inputs = map(int, raw_input().split())
list = [0] * n
for i in range(inputs):
    x, y, incr = map(int, raw_input().split())
    list[x-1] += incr
    if(y < n): 
        list[y] -= incr
        
        
max_val = total = 0
for i in list:
    total = total + i;
    if max_val < total: 
        max_val = total
print max_val