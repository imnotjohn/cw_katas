def series_sum(n):
    values = []
    if n > 0:
        for x in range(1,n+1):
            if x == 1:
                den = 1
            else:
                den += 3
            values.append(1/float(den))
        total = round(sum(values),2)
        return "%.2f" % (total)
    else:
        return "%.2f" % 0.00
#n = 1 ==> 1 / 1*n + 0
#n = 2 ==> 1 / 2*n + 1
#n = 3 ==> 1 / (2*n + 1)
#n = 4 ==> 1 / (2*n + 1)
