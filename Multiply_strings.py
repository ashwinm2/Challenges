# Multiply two strings.
class Solution(object):
    def multiply(self, num1, num2):
        high = len(num2) - 1
        index = high
        total = 0
        while index >= 0:
            denom = int(num2[index])
            low = len(num1) - 1
            jndex = low
            step = 0
            carry = 0
            while jndex >= 0:
                num = int(num1[jndex])
                val = (denom * num) + carry
                if val > 10 and jndex != 0:
                    carry = val / 10
                    val = val % 10
                else: 
                    carry = 0
                step += val * (10 ** (low - jndex))
                jndex -= 1
            total += step * (10 ** (high - index))
            index -= 1
            
        return str(total)