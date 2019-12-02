#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0

    if len(s)==1 and sum(s)==d:
        return 1


    for i in range(len(s)-m+1):
        if sum(s[i:i+m])==d:
            count+=1
        print((i,i+m),(s[i:i+m]),sum(s[i:i+m]))    
    return count




n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)

print(result)
