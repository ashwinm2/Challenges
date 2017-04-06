# implementing atoi

class Solution(object):
    def myAtoi(self, str):
    #    try:
        i = 0
        act = []
        l = len(str)
        while i < l and str[i] == " ":
            i += 1
        
        if i < l:
            if str[i] == "+" or str[i] == "-":
                act.append(str[i])
                i += 1
        
        while i < l and str[i].isdigit():
            act.append(str[i])
            i += 1
        
        print act
        final = 0
        if act != []:
            if act[0] == "-":
                flag = -1
                act = act[1:]
            elif act[0] == "+":
                flag = 1
                act = act[1:]
            else:
                flag = 1
            
            
            if act != []:
                while act:
                    if act[0].isdigit():
                        temp = ord(act[0]) - ord('0')
                        final = temp + final * 10
                        act = act[1:]
                    else:
                        return 0
                
                print final
                final = final * flag
                if final > 2147483647:
                    return 2147483647
                elif final < -2147483648:
                    return -2147483648
                else:
                    return final
            else:
                return 0
        else:
            return 0