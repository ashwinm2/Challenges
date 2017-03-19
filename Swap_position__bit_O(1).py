# Swap positions of bit in O(1)
bin = int(raw_input(), 2)
print "{0:b}".format(bin)
sam = bin
len = 0
while 1 < sam:
  sam = sam >> 1
  len = len + 1
  
even = ''
for i in range(0, len):
  even += 'a'

even = int(even, 16)
odd = even >> 1

even = bin & even
odd = bin & odd
odd = odd << 2
even = even | odd
even = even >> 1
print "{0:b}".format(even)