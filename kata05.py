#You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

def find_outlier(integers):
    p = integers[0]%2
    if integers[1]%2 != p:
        if integers[2]%2 != p:
            return integers[0]
        return integers[1]
    else:
        for i in integers:
            if i%2 != p:
                return i
    # if (integers[i]%2 == 0): #if first index value is even
    #     if (integers[i+1]%2 == 0): #check if second index value is also even
    #         for i in range(len(integers)-1):
    #             while(integers[i]%2 == 0): #if it is, loop
    #                 i += 1
    #             return integers[i]
    #     elif ((integers[i+1]%2 != 0) & (integers[len(integers)-1]%2 != 0)): #first value is even, but second and last are not
    #         return integers[i]
    #     else: #first is even, but second and last values are not both odd
    #         for i in range(i+1,len(integers)-1):
    #             while(integers[i]%2 != 0):
    #                 i += 1
    #                 return integers[i]
    # else: #first value is odd,
    #     if (integers[i+1]%2 != 0): #check if second value is also odd
    #         for i in range(i+1,len(integers)-1):
    #             while(integers[i]%2 != 0):
    #                 i += 1
    #             return integers[i]
    #     else: #first value is odd, and second value is even
    #         for i in range(len(integers)-1):
    #             while(integers[i]%2 == 0): #if it is, loop
    #                 i += 1
    #             return integers[i]
