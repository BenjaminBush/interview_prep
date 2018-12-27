# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?

import numpy as np

def hackyrotate(matrix):
    return np.transpose(np.flip(matrix, 0))

def rotate(matrix):
    # for half of the layers:
    #   temp = top_layer
    #   top_layer = left_layer
    #   left_layer = bottom_layer
    #   bottom_layer = right_layer
    #   right_layer = temp

    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer                                           # first and last correspond to first and last index of layer of onion of matrix
        last = n - 1 - layer
        for i in range(first, last):                            # we don't swap the whole rows/cols at once, but element by element (i)
            offset = i - layer                                  # offset helps us keep track of these elements for indxing>???
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[last-offset][layer]
            matrix[last-offset][layer] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = temp
    return matrix

def ben_rotate(matrix):
    """
    1) for each column, reverse the row elemnts
    2) transpose
    """
    flip = ben_flip(matrix)
    return flip

def ben_flip(matrix):
    # 1) transpose, 2) reverse each row (originally column)
    matrix = ben_transpose(matrix)
    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]

    return matrix


def ben_transpose(matrix):
    return [*zip(*matrix)]


def print_matrix(matrix):
    for r in matrix:
        for c in r:
            print(c, end=" ")
        print()

if __name__ == "__main__":
    matrix = [[11, 12, 5, 2], [15, 6, 10, 9], [10, 8, 12, 5], [12, 15, 8, 6]]
    n = np.array([[11, 12, 5, 2], [15, 6, 10, 9], [10, 8, 12, 5], [12, 15, 8, 6]], int)
    print(n)
    print()
    r = ben_rotate(matrix)
    print_matrix(r)
    print()
    m = hackyrotate(n)
    print(m)