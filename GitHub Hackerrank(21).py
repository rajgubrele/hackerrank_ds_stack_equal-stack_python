#!/usr/bin/env python
# coding: utf-8

# **HackerRank---> DataStructure --->Stack--->Equal Stack ---> Python**
# 
# 
# **Problem:** You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# 
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.
# 
# **Example**
# h1 = [1,2,1,1]
# h2 = [ 1,1,2]
# h3= [1,1]
# 
# There are 4,3 and 2 cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from **h1** (heights = [1, 2]) and from **h2** (heights = [1, 1]) so that the three stacks all are 2 units tall. Return **2** as the answer.
# 
# Note: An empty stack is still a stack.

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3= h3[::-1]
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    
    
    while True:

        mini = min(sum1,sum2,sum3)
        if mini == 0:
            return 0
            
        if  sum1 > mini:
            sum1 -=h1.pop()
        if sum2 > mini:
            sum2 -= h2.pop()
        if sum3 > mini:
            sum3 -=h3.pop()
        if sum1==sum2==sum3:
            return sum1
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
 

