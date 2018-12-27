# Write an algorithm such that if an element in an MxN matrix is 0, its entire ro and column are set to 0

def zeroify(matrix):
    flagged_rows = []
    flagged_cols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                flagged_rows.append(i)
                flagged_cols.append(j)


    for row in flagged_rows:
        matrix = nullify_row(matrix, row)
    for col in flagged_cols:
        matrix = nullify_col(matrix, col)

    return matrix

def nullify_row(matrix, row):
    for col in range(len(matrix[0])):
        matrix[row][col] = 0
    return matrix

def nullify_col(matrix, col):
    for row in range(len(matrix)):
        matrix[row][col] = 0
    return matrix

def print_matrix(matrix):
    for r in matrix:
        for c in r:
            print(c, end=" ")
        print()

if __name__ == "__main__":
    matrix = [[11, 12, 5, 0], [15, 6, 10, 9], [10, 8, 12, 5], [12, 15, 8, 6]]
    print_matrix(matrix)
    print()
    matrix = zeroify(matrix)
    print_matrix(matrix)