
"""
Write heap functions to build heap, add new element in heap.
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
        

def main():

    #arr = [41 ,79 ,84 ,38 ,33 ,81 ,17, 15 ,61 ,6] 
    arr = [5, 10, 15, 20, 32, 54, 35, 56, 52, 22, 13, 87, 30, 25]

    min_h, max_h = [i for i in arr], [i for i in arr]

    build_min_heap(min_h)
    build_max_heap(max_h)

    print("array: ", arr)
    print("min_heap: ", min_h)
    print("max_heap: ", max_h)
    print("")

    item = 100

    print("Inserted: " + str(item))
    insert_into_min_heap(min_h, item)
    insert_into_max_heap(max_h, item)

    print("min_heap: ", min_h)
    print("max_heap: ", max_h)
    print("")

main()
