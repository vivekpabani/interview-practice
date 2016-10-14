import math

"""

Find number of inversions in an array. Inversion means a pair where a[i] > a[j] and i <j in
O(nlogn).

"""


def  merge(l, left, mid, right):
    
    i, j = left, mid
    inv_c = 0

    temp = list()

    # iterate through both halves of the list
    # if the value in left half is smaller, add it to the temp
    # if the value in the right half is smaller, then add it. In addition, count the inversion.
    # the number of inversions will be the number of elements to the right of current element in left half.  

    while i <= mid-1 and j <= right:
        if l[i] <= l[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            inv_c = inv_c + mid - i
            j += 1

    # add remaining elements to the temp
    while i <= mid-1:
        temp.append(l[i])
        i += 1

    while j <= right:
        temp.append(l[j])
        j += 1

    #replace l's corresponding part with sorted temp list.
    k = 0
    for i in range(left, right+1):
        l[i] = temp[k]
        k += 1   

    return inv_c
    

def merge_sort(l, left, right):

    inv_c = 0
    if left < right:
        mid = int((left+right)/2)
        inv_c += merge_sort(l, left, mid)
        inv_c += merge_sort(l, mid+1, right)
        inv_c += merge(l, left, mid+1, right)

    return inv_c


def main():

    arr = [7, 5 ,1, 2, 3]

    print(merge_sort(arr, 0, len(arr) -1)) 

main()
