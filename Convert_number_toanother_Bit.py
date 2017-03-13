# Converting a number to A to B using Bit manipulation
p, n = map(int, raw_input().split())
print p, n
print "{0:b}".format(p), "{0:b}".format(n)
temp = p ^ n 
a = 1
i = 0
count = 0

# To find the length of a binary number or the most significant bit
samp = temp
j = 1
# print "{0:b}".format(temp)
while 1 < samp:
  samp = samp >> 1
  j = j + 1

while i < len("{0:b}".format(temp)):
  if (temp & (a << i)) == (a << i):
    count = count + 1
    i = i + 1
  else:
    i = i + 1
print count