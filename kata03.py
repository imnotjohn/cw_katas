###  Takes that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

def find_even_index(arr):
    sum_left, sum_right, index = 0, 0, 0

    while index <= len(arr)-1:
        # print ("L: %d\t\tR: %d\t\ti: %d") % (sum_left, sum_right, index)
        sum_left = sum(arr[:index])
        sum_right = sum(arr[index+1:])
        if sum_left == sum_right:
            return index
        else:
            index += 1
    return -1
