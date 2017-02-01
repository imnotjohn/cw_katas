# Your task is to write a function maskify, which changes all but the last four characters into '#'.
# Kata: maskify

def maskify(cc):
    # s = ""
    # if len(cc) >= 5:
    #     for char in range(0, len(cc)-4):
    #         s += "#"
    #     return s + cc[-4:]
    # else:
    #     return cc
    return (("#"*len(cc[:-4]) + cc[-4:]) if (len(cc) >= 5) else cc)
