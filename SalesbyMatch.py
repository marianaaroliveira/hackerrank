#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):#number of total socks, list with the color of each sock
    #return the number of pairs
    #run a loop through the list
    #run a second loop from the next index
    #replace the sock that already was counted with a 0
    count = 0#this variable is going to be used to store the number of pairs
    if n>=1 and n<=100:#we need to check if n is between 1 and 100
        for i in range(n):#the last one is not going to be process
            if ar[i]>=1 and ar[i]<=100:
                for l in range(i+1, n):
                    if ar[i]==ar[l]:
                        #print(i)
                        #print(ar[i])
                        #print(ar[l])
                        #print(l)
                        count = count + 1
                        ar[l]=0
                        break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
