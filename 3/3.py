#!/usr/bin/python3


def combine_intervals(il):

    endpoints = dict()

    for start in (i[0] for i in il):
        endpoints[start] = endpoints.setdefault(start, 0) + 1

    for end in (i[1] + 1 for i in il):
        endpoints[end] = endpoints.setdefault(end, 0) - 1

    #print(endpoints.items())

    return sorted(filter(lambda kv: kv[1] != 0, endpoints.items()))


def nthsmall(n, il):

    limits = combine_intervals(il)
    print(limits)
    cum, count, index = 0, 0, 0

    here = limits[0][0]

    while index < len(limits):

        size = limits[index][0] - here

        if n < cum + size * count:
            return here + (n - cum) / count

        cum = cum + count * size
        count = count + limits[index][1]
        here = here + size
        index = index + 1


print(nthsmall(6, [[1, 5], [2, 4], [7, 9]]))

