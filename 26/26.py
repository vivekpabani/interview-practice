

"""

Find equilibrium index in array. Its the index i where sum till i from 0th index = sum from ith
index to last index.

"""


def find_equ(arr):

    """
    set the total as sum of array.
    left total as 0.
    at every step, add an item to left sum, and deduct from total (kind of right sum)
    if both left and right are equal, print the index and sub arrays.
    """
 
    total = sum(arr)
    left_s = 0

    i = 0

    if left_s == total:
        print(i, arr[:i], arr[i:])

    for i in range(len(arr)):
        left_s += arr[i]
        total -= arr[i]
        if left_s == total:
            print(i+1, arr[:i+1], arr[i+1:])
     

def main():

    arr = [-7, 1, 5, 2, -4, 3, 0]
    find_equ(arr)


main()
