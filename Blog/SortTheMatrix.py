__author__ = 'trunghieu11'

def sortMatrix(matrix):
    counter = [0 for i in range(0, 10**6)]

    # step 1. get all items in matrix and add to array
    # step 2. sort this array by ascending
    for row in matrix:
        for x in row:
            counter[x] += 1

    # step 3. try to put all items back to the matrix
    total_row = len(matrix)
    total_column = len(matrix[0])

    row_index = 0
    column_index = 0
    array_index = 0
    i = 0

    # while we still not reach the bottom right cell in matrix
    while row_index < total_row and column_index < total_column:
        while counter[array_index] <= 0:
            array_index += 1

        # put back to the matrix
        matrix[row_index - i][column_index + i] = array_index
        counter[array_index] -= 1

        # increase i.
        i += 1

        # if reached the first row, go to next diagonal
        if row_index - i < 0 or column_index + i >= total_column:
            i = 0

            if row_index + 1 < total_row:
                row_index += 1
                column_index = 0
            else:
                column_index += 1

    return matrix


if __name__ == '__main__':
    matrix = [
        [1, 4, 5],
        [3, 2, 4],
        [6, 4, 3],
        [7, 8, 9],
        [10, 12, 14]
    ]
    matrix = sortMatrix(matrix)
    for row in matrix:
        print ' '.join(str(x) for x in row)

    # counter = [0 for i in range(10**6)]
    # for row in matrix:
    #     for x in row:
    #         counter[x] += 1
    # printArray(counter)