def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # diag_list = []
    # count = len(matrix)
    # coordinate_x = 0
    # coordinate_y = 0

    # while count > 0:
    #     diag_list.append(matrix[coordinate_y][coordinate_x])
    #     coordinate_x += 1
    #     coordinate_y += 1
    #     count -= 1
    
    # return sum(diag_list)

    total = 0

    for lst in range(len(matrix)):
        total += matrix[lst][lst]
        total += matrix[lst][-1 - lst]

    return total


        
