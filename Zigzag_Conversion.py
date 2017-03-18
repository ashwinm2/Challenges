def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    final = ""
    full_l = len(s)
    i = 0
    first_ser = []
    while i < full_l:
        first_ser.append(i)
        if numRows > 2:
            i += numRows + numRows - 2
        else:
            if numRows == 2:
                i += numRows
            else:
                i += 1
    
    first_ser.append(i)
    #print first_ser
    for ele in range(0,numRows):
        temp = ""
        for i in first_ser:
            #print "Iteration level", ele, "First series", i 
            if ele == numRows - 1:
                forw = i + ele
                if  forw < full_l:
                    temp += s[forw]
            else:
                back = i - ele 
                forw = i + ele
                if back == forw:
                    if back >= 0 and back < full_l:
                        temp += s[back]
                else:
                    if  back >= 0 and back < full_l:
                        temp += s[back]
                    if forw < full_l: 
                        temp += s[forw]
        #print "Current", temp
        final = final + temp
        #print final
    #print final
    return final