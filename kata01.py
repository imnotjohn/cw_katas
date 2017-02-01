# returns boolean value of whether or not
# amount of X/x == O/o

def xo(s):
    x_count = 0
    o_count = 0
    for each_letter in s:
        if (each_letter == "x") | (each_letter == "X"):
            x_count += 1
        elif (each_letter == "o") | (each_letter == "O"):
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False

xo("zLlz")
