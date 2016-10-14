

def partition(arr, i, calculated):

    # base case: when all elements are either added or skipped, return the difference. 
    if i == -1:
        return abs(calculated - abs(sum(arr)-calculated)) 

    # or return the min of two possibility - adding current element, and skipping current element.
    return min(partition(arr, i-1, calculated+arr[i]), partition(arr, i-1, calculated))


def main():

    #arr = [1, 6, 5, 11]
    #arr = [2, 10,3,8,5,7,9,5,3,2]
    arr = [771,121,281,854,885,734,486,1003,83,62]

    print(partition(arr, len(arr)-1, 0))


main()
