# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



def generate(numRows):

    if numRows == 0:
        return []
        
    triangle = [[1]]
    
    for i in range(1, numRows):
        triangle.append([])
        for j in xrange(i+1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                sum = triangle[i-1][j-1] + triangle[i-1][j]
                triangle[i].append(sum)
    
    return triangle

def getRow(rowIndex):

    triangle = [[1]]
    
    for i in range(1, rowIndex+1):
        triangle.append([])
        for j in xrange(i+1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                sum = triangle[i-1][j-1] + triangle[i-1][j]
                triangle[i].append(sum)
    
    return triangle[rowIndex]

