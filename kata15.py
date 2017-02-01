def findOddInt(seq):
    d = dict((eachInt, seq.count(eachInt) %2 != 0) for eachInt in set(seq))
    return next(key for key, value in d.iteritems() if value == True)

#kiss
def find_it(seq):
    for i in seq:
        if seq.count(i) %2 is not 0:
            return i
