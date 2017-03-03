# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    spiral = []
    i = j = 0
    bounds = 0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] != None:
                circle(i, j, matrix, spiral, bounds)
                bounds += 1
    return spiral

def circle(i, j, matrix, spiral, bounds):
    
    if i > len(matrix)-1-bounds or i < bounds:
        return
    if j > len(matrix[i])-1-bounds or j < bounds:
        return
    if matrix[i][j] == None:
        return
    
    spiral.append(matrix[i][j])
    matrix[i][j] = None
    if i == bounds:
        circle(i, j+1, matrix, spiral, bounds)
    if j == len(matrix[i])-1-bounds:
        circle(i+1, j, matrix, spiral, bounds)
    if i == len(matrix)-1-bounds:
        circle(i, j-1, matrix, spiral, bounds)
    if j == bounds:
        circle(i-1, j, matrix, spiral, bounds)

matrix = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
]
print spiralOrder(matrix)
