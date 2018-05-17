# Program print/return changed array , as for x, y grid
# You can think of grid[x][y] as being the character at the
# x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin will be in the upper-left corner,
# the x-coordinates increase going right,
# and the y-coordinates increase going down.

grid1 = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

grid2 = [['a', '1', 'c', '.', '.'],
         ['b', '2', 'O', '3', '.'],
         ['f', '3', 'w', '.', '.']]


def flipped_coordinates(matrix):
    new_list = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        k = len(matrix) - 1
        for j in range(len(matrix)):
            new_list[i][j] = matrix[k][i]
            k -= 1
    # print list
    """
    for row in new_list:
        print(' '.join([str(elem) for elem in row]))
    """
    # better to use
    print('\n'.join(map(''.join, zip(*matrix))))
    return new_list


flipped_coordinates(grid1)
print("")
flipped_coordinates(grid2)
