# Pairs

def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    answer = 0
    total = {}
    for i in a:
        if i + k in total or i - k in total:
            if i + k in total and i - k in total:
                answer += 2
            else:
                answer += 1
        total[i] = 1
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
