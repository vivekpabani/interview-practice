#!/usr/bin/python3

"""
Problem Statement:

Generate power set of given set.

"""

def power_set(s):
    """
    returns the powerset of given set s
    """

    s_l = list(s)
    p = list()

    # length of the powerset
    p_len = pow(2, len(s_l))

    # iterate through the length of powerset. Each number converted to binary 
    # represents if the ith element of the set should be in the subset or not.

    for i in range(p_len):
        temp_s = set()
        for j in range(len(s_l)):
            if (i>>j) & 1:
                temp_s.add(s_l[j])
        p.append(temp_s)

    return p


def main():

    s = set([1, 2, 3])

    print(power_set(s))

if __name__ == "__main__":
    
    main()

