#Sort an array by value and index
# Sort an array by value and index
#
# Your task is to sort an array of integer numbers by the product of the value and the index of the positions.
#
# For sorting the index starts at 1, NOT at 0!
# The sorting has to be ascending.
# The array will never be null and will always contain numbers.

import operator
def sort_by_value_and_index(arr):
    storage = {}
    value = 0
    sorted_arr = []
    for i, v in enumerate(arr):
        value = (i+1)*v
        storage[i] = value
    sorted_storage = dict(sorted(storage.items(), key=operator.itemgetter(1)))
    for key in sorted_storage:
        sorted_arr = arr[key]
    return sorted_arr
