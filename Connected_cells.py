# Connected Cells in a Grid
def find(key, connected):
    temp = 1
    connected.pop(key, None)
    if (key[0]-1, key[1]) in connected:
        temp += find((key[0]-1, key[1]), connected)
    if (key[0]-1, key[1]-1) in connected:
        temp += find((key[0]-1, key[1]-1), connected)
    if (key[0], key[1]-1) in connected:
        temp += find((key[0], key[1]-1), connected)
    if (key[0]+1, key[1]-1) in connected:
        temp += find((key[0]+1, key[1]-1), connected)
    if (key[0]+1, key[1]) in connected:
        temp += find((key[0]+1, key[1]), connected)
    if (key[0]+1, key[1]+1) in connected:
        temp += find((key[0]+1, key[1]+1), connected)
    if (key[0], key[1]+1) in connected:
        temp += find((key[0], key[1]+1), connected)
    if (key[0]-1, key[1]+1) in connected:
        temp += find((key[0]-1, key[1]+1), connected)
    return temp
    
n = int(raw_input())
m = int(raw_input())
total = []
connected = {}
for i in xrange(n):
    temp = raw_input().split(' ')
    for j in xrange(m):
        if temp[j] == '1':
            if (i,j) not in connected:
                connected[(i,j)] = 0
    total.append(temp)

tot = 0
while connected != {}:
    key, value = connected.popitem()
    temp = find(key, connected)
    if tot < temp:
        tot = temp

print  tot  
