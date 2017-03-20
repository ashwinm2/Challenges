def f(x, y):
    hashmap = { 0: {1:"I", 4: "IV",5:"V", 9:"IX"},
        1: {1:"X", 4: "XL",5:"L", 9:"XC"},
        2: {1:"C", 4: "CD",5:"D", 9:"CM"},
        3: {1:"M"},
        }
    return hashmap[x][y]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)[::-1]
        l = len(num)
        total = ""
        for i in range(0, l):
            no = int(num[i])
            temp = ""
            if no < 4:
                base = f(i, 1)
                for j in range(0,no):
                    #print "Times"
                    temp += base
            elif 5 < no < 9:
                temp = f(i, 5)
                base = f(i, 1)
                for j in range(5,no):
                    temp += base
            else:
                temp = f(i, no)
            total = temp + total
        print total
        return total