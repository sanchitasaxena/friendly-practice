matrix = [[9,4,0,9,8], [3,4,5,2,4], [0,0,0,0,0],[4,3,21,3,0]]



def zero_matrix(matrix):

    i = 0
    j = 0
    row = None
    column = None

    height = len(matrix)
    width = len(matrix[0])


    # iterate through the matrix, find a zero within each row [i][j]
        # if you find a zero, take row [i] and make all elements zero
            # then you need to increment by i, and at that same j
            # go through all i's and set that j element to zero
        # then you need to increment go back to the original i, and increment,
        # search through js, until you find zero again

    while i < height and j < width:
        if matrix[i][j] == 0:
         
            for elem in matrix[i]:
            # all elements in row i need to be set to zero
                elem = 0
            # for all j set = 0 at that i
            for l in matrix:
                matrix[l][j] = 0

            i +=1
        else:
            j +=1

    return matrix








print zero_matrix(matrix)

