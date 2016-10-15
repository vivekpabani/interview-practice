
"""
A stream of integers is coming. Find median of numbers received till now. 
"""


def parent(i):

    return int(i/2)


def left(i):

    return 2*i + 1


def right(i):

    return 2*i + 2


def max_heapify(arr, i):

    """
    assumes that left and right subtrees of i are max heaps. only i is misplaced.
    so puts the ith item in correct place
    """

    l = left(i)
    r = right(i)

    if l <= len(arr)-1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r <= len(arr)-1 and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest) 


def build_max_heap(arr):

    """
    Given an array, builds the max heap
    """

    for i in range(int((len(arr)-1)/2), -1, -1):
        max_heapify(arr, i)
        

def insert_into_max_heap(max_h, key):

    """
    inserts the new element as the leaf, and then promotes it up till its correct position.
    """

    max_h.append(key)

    i = len(max_h)-1
    while i > 0 and max_h[parent(i)] < max_h[i]:
        max_h[parent(i)], max_h[i] = max_h[i], max_h[parent(i)]
        i = parent(i)


def min_heapify(arr, i):

    l = left(i)
    r = right(i)

    if l <= len(arr)-1 and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i

    if r <= len(arr)-1 and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest) 


def insert_into_min_heap(min_h, key):

    min_h.append(key)

    i = len(min_h)-1
    while i > 0 and min_h[parent(i)] > min_h[i]:
        min_h[parent(i)], min_h[i] = min_h[i], min_h[parent(i)]
        i = parent(i)


def build_min_heap(arr):

    for i in range(int((len(arr)-1)/2), -1, -1):
        min_heapify(arr, i)
        

def find_median(min_h, max_h, item):

    """
    inserts the item in appropriate heap.
    if height difference is at most 1, finds and returns median.
    otherwise balances and then returns median. 
    """

    if len(max_h) == 0 or item < max_h[0]:
        insert_into_max_heap(max_h, item)
    else:
        insert_into_min_heap(min_h, item)

    diff = len(max_h) - len(min_h)

    if diff == 0:
        m = (max_h[0] + min_h[0])/2
    elif diff == -1:
        m = min_h[0]
    elif diff == 1:
        m = max_h[0]
    elif diff == -2:
        insert_into_max_heap(max_h, min_h[0])
        del(min_h[0])
        build_min_heap(min_h)
        m = (max_h[0]+min_h[0])/2
    elif diff == 2:
        insert_into_min_heap(min_h, max_h[0])
        del(max_h[0])
        build_max_heap(max_h)
        m = (max_h[0]+min_h[0])/2
            
    return m
            

def main():

    #arr = [41 ,79 ,84 ,38 ,33 ,81 ,17, 15 ,61 ,6] 
    arr = [5, 10, 15, 20, 32, 54, 35, 56, 52, 22, 13, 87, 30, 25]

    min_h, max_h = list(), list() 
    l = list()

    for item in arr:
        l.append(item)
        l = sorted(l)
        m = find_median(min_h, max_h, item) 
        print("Inserted: " + str(item))
        print("Items so far: ", l)
        print("Median: " + str(m))
        print("")
main()
