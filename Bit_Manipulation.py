# Bit Manipulation between a given range
binary_n = int(raw_input(),2)
binary_m = int(raw_input(),2)
i = int(raw_input())
j = int(raw_input())
most_sig_bit = binary_n >> (j + 1)
most_sig_bit = most_sig_bit << (j + 1)
least_sig_bit = binary_n & (2**i - 1)
temp = most_sig_bit | least_sig_bit
binary_m = binary_m << i
temp = temp | binary_m
# print temp
p = "{0:b}".format(temp)
print p