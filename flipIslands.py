# Given a two d matrix containing 1’s and 0’s, capture the groups of zeros completely surrounded by ones.

# A group of zeros is captured by flipping all 0’s into 1's in that group. 

# For example,

1 1 1 1
1 0 0 1
1 1 0 1
1 0 1 1

1 1 1 1
1 1 1 1
1 1 1 1
1 0 1 1


def matrix(arr):
    for edge in xrange(len(arr[0])
        if arr[0][edge] == 0:
 #           arr[0][edge] = -1
             flip(arr, 0, edge)
    for edge in xrange(len(arr)):
        if arr[edge][0] == 0:
 #           arr[edge][0] = -1
             flip(arr, edge, 0)
    for edge in xrange(len(arr[len(arr)-1]):
        if arr[len(arr)-1][edge] === 0:
 #           arr[len(arr)-1][edge] = -1
             flip(arr, len(arr)-1, edge)
    for edge in xrange(len(arr)):
        if arr[edge][len(arr[edge])] == 0:
#            arr[edge][len(arr[edge])] = -1
            flip(arr, edge, len(arr[edge])
         


def flip(arr, i, j):
    if arr[i][j] == 1:
        return
    if i < 0 or i > len(arr)-1:
        return
    if j < 0 or j > len(arr[i])-1:
        return
    arr[i][j] = -1
    flip(i+1, j)
    flip(i-1, j)
    flip(i, j+1)
    flip(i, j-1)
        
        

                