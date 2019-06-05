import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    revArray = list(reversed(arr))
    numOne = 0
    numTwo = 0
    
    for i in range(len(arr)):
        numOne += arr[i][i]

    for i in range(len(arr)):
        numTwo += revArray[i][i]

    return abs(numOne - numTwo)
    




if __name__ == '__main__':
    
    arr = [[11,2,4],[4,5,6],[10,8,-12]]

    result = diagonalDifference(arr)
    print(result)

    