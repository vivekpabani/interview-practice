import sys


def main():

    a = [1, 3, -4, 10, 6, 9, -5, -2, -9]

    # seperate the negative and positive numbers and sort.
    a_n = sorted([i for i in a if i<0], reverse=True)
    a_p = sorted([i for i in a if i>0])

    #for both negative and positive array, create a sum matrix which has sum of all i to j indices.

    an_s = [[None for i in range(len(a_n))]for j in range(len(a_n))] 

    for i in range(len(a_n)):
        for j in range(i, len(a_n)):
            if i==j:
                an_s[i][j] = a_n[i]
            else:
                an_s[i][j] = an_s[i][j-1] + a_n[j] 

    ap_s = [[None for i in range(len(a_p))]for j in range(len(a_p))] 

    for i in range(len(a_p)):
        for j in range(i, len(a_p)):
            if i==j:
                ap_s[i][j] = a_p[i]
            else:
                ap_s[i][j] = ap_s[i][j-1] + a_p[j] 

    # go through negative sum matrix row by row
    # for each value, find a value that adds up to 0.
    # if found, print those ranges. 
    # if sum exceeded, skip that row for further calculation
    #(since the sum will always increase when you go left to right in any  row.

    for i in range(len(a_n)):
        for j in range(i, len(a_n)):
            for k in range(len(a_p)):
                for l in range(k, len(a_p)):
                    ans = an_s[i][j] + ap_s[k][l]
                    if ans > 0:
                        break
                    if ans == 0:
                        print(a_n[i:j+1], a_p[k:l+1])
main()
