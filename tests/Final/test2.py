'''
Example 1: if n is 5, the output should be:
[[0 1 0 1 0]
[1 0 1 0 1]
[0 1 0 1 0]
[1 0 1 0 1]
[0 1 0 1 0]]
Example 2: if n is 6,
the output should be:
[[0 1 0 1 0 1]
[1 0 1 0 1 0]
[0 1 0 1 0 1]
[1 0 1 0 1 0]
[0 1 0 1 0 1]
[1 0 1 0 1 0]]
'''
import numpy as np
#size = int(input("Enter the size of the n by n board: "))
# The missing code goes here, but write it below
n = 3
arry = [[0,1,0,1],[0,1,0,1]]
checkers = np.zeros((n, n))
checkers[::2, 1::2] = 1
checkers[1::2, ::2] = 1

print(checkers)
