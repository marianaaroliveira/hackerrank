#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr1
#  2. INTEGER_ARRAY arr2
#

def minimumMoves(arr1, arr2):
    #is going to sabe the number of moves needed
    count = 0
    # length of the arrays
    larr1 = len(arr1)
    larr2 = len(arr2)
    if larr1 == larr2:#we need to check if they have the same length
        if larr1>=1 and larr1<=(10**5):#we need to check if lenght is between 1 and 10^5
            for i in range(larr1):#first we going to run a loop on the array larr1
                #second we going to creat variables with str of the number that way we can manipulate
                str1 = str(arr1[i])
                str2 = str(arr2[i])
                if str1 != str2 and len(str1) == len(str2):#if they are different and they have the same length then we need to modify
                     #print(str1)
                     #print(str2)
                     #print(len(str1))
                     for c in range(len(str1)):
                        #lets tranform them into int again
                        #print(str1[c])
                        #print(str2[c])
                        int1 = int(str1[c])
                        int2 = int(str2[c])
                        #we need to stay in the loop while until the number is equal
                        while(int1 != int2):
                            if int1 < int2:#in case it's smaller than we need to increment
                                int1 = int1 + 1
                                count = count + 1
                            elif int1 > int2:#in case it's bigger than we need to decrement
                                int1 = int1 - 1
                                count = count +1
    return count                         
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr1_count = int(input().strip())

    arr1 = []

    for _ in range(arr1_count):
        arr1_item = int(input().strip())
        arr1.append(arr1_item)

    arr2_count = int(input().strip())

    arr2 = []

    for _ in range(arr2_count):
        arr2_item = int(input().strip())
        arr2.append(arr2_item)

    result = minimumMoves(arr1, arr2)

    fptr.write(str(result) + '\n')

    fptr.close()
