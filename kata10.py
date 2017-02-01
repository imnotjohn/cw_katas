def longest_consec(strarr, k):
    n = len(strarr)
    if (n == 0) | (k > n) | (k <= 0):
        return ""
    else:
        strarr.sort(key=len, reverse=True)
#         strarr.sort(key=lambda item: (-len(item), item))
        finalstr = ""
        for i in range(0,k):
            print(i)
            finalstr += strarr[i]
        return finalstr
