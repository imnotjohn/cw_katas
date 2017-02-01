# In a DNA String:
# "A" and "T" are compliments of eachother
# "C" and "G" are compliments of eachother
# will read in initial DNA String
# will return compliment String
# ex: DNA_strand("ATTGC") # return "TAACG"

def DNA_strand(dna_str):
    ### my solutioN:
    # convert_list = list(dna_str)
    # output_str = []
    # for each in convert_list:
    #     if each == "T":
    #         output_str.append("A")
    #     elif each == "A":
    #         output_str.append("T")
    #     elif each == "C":
    #         output_str.append("G")
    #     elif each == "G":
    #         output_str.append("C")
    # return "".join(output_str)

    ### top solution:
    #Python3
    #return dna_str.translate(str.maketrans("TACG", "ATGC"))

    ### top solution [python2]
    # use dictionary 
    pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([pairs[x] for x in dna_str])
