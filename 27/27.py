

"""

Find the Minimum length Unsorted Subarray, sorting which makes the complete array
sorted. Eg: ( 0 4 12 3 15 16 18 17 19} it should be 12 and 17.

"""


def find_unsorted_subarray(arr):

    s, e = 0, len(arr)-1 

    i = 0

    while i < len(arr)-1:
        if arr[i+1] < arr[i]:
            s = i
            break
        i += 1

    i = len(arr)-1 

    while i > 0:
        if arr[i-1] > arr[i]:
            e = i
            break
        i -= 1

    max_a, min_a = max(arr[s:e+1]), min(arr[s:e+1])

    for i in range(0, s):
        if arr[i] > min_a:
            s = i
            break

    for i in range(len(arr)-1, e, -1):
        if arr[i] < max_a:
            e = i
            break 

    return s, e


def main():

    #arr = [0,4,12,3,15,16,18,17,19]
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    s, e = find_unsorted_subarray(arr)
    print(s, e)
    print(arr[s:e+1])


main()
