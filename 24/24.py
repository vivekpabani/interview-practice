

"""

Triplet sum problem. Find all pairs of numbers such that a[i]+a[j]+a[k]=N.

"""


def find_3elem(arr, n):

    arr = sorted(arr)

    # keeping one element constant, find two elements which sum to n - constant.

    for i in range(len(arr)-2):

        j, k = i+1, len(arr)-1

        while j < k:
            ans = arr[i] + arr[j] + arr[k]
            if ans == n:
                print(arr[i], arr[j], arr[k])
                j, k = j + 1, k - 1
            elif ans > n:
                k = k - 1
            else:
                j = j + 1 


def main():

    arr = [1, 4, 45, 6, 10, 8]
    n = 22

    find_3elem(arr, n)


main()
