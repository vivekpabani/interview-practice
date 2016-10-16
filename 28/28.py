
"""
Numbers in array are repeated thrice except one number which is present just once. Find
the one?
"""

def find_unique(arr):

    ones, twos = 0, 0

    for item in arr:

        # The expression "one & arr[i]" gives the bits that are
        # there in both 'ones' and new element from arr[].  We
        # add these bits to 'twos' using bitwise OR

        twos = twos | (ones & item) 
 
        # XOR the new bits with previous 'ones' to get all bits
        # appearing odd number of times

        ones = ones ^ item

        # The common bits are those bits which appear third time
        # So these bits should not be there in both 'ones' and 'twos'.

        common_ones_twos = ~(ones & twos)

        # Remove common bits (the bits that appear third time) from ones and twos

        ones = ones & common_ones_twos

        twos = twos & common_ones_twos

    return ones


def main():

    # arr = [3, 3, 2, 3]
    arr = [12, 3, 4, 4, 2, 3, 12, 3, 12]
    unique = find_unique(arr)

    print(unique)


main()
