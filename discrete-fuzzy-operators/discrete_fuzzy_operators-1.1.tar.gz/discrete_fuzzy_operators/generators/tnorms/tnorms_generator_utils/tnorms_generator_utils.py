import numpy
from typing import List


def generate_increasing_rows(min_value: int,
                             max_value: int,
                             max_vector_size: int,
                             recursive_step: int = 0,
                             row_list: List = None) -> List[int]:
    """
    A generator which builds are possible vectors of a certain size (max_vector_size) that are increasing, where its
    entries are taken from a range (the discrete interval [min_value, max_value]).

    Args:
        min_value: An integer, representing the minimum value of the entries of the vector.
        max_value: An integer, representing the maximum value of the entries of the vector.
        max_vector_size: An integer, representing the size of the vector to be generated.
        recursive_step: An integer, representing the number of recursive calls. It is used as the stop criteria.
        row_list: A list of integers, representing the generated vector.

    Returns:
        A list of integers, representing the vector with size max_vector_size and which entries are in increasing order.
    """
    if row_list is None:
        row_list = []

    if recursive_step == max_vector_size:
        yield row_list
    else:
        for i in range(min_value, max_value + 1):
            new_row = row_list.copy()
            new_row.append(i)
            yield from generate_increasing_rows(min_value=i,
                                                max_value=max_value,
                                                max_vector_size=max_vector_size,
                                                recursive_step=recursive_step + 1,
                                                row_list=new_row)


def generate_symmetric_matrix(rows: List[List]) -> numpy.ndarray:
    """
    Generates a symmmetric matrix from a upper triangular matrix.

    Args:
        rows: A list of lists, containing the staggered rows of the matrix; that is, the first list has k elements,
        the second list has k-1, and so on.

    Returns:
        A symmetric matrix, generated from the staggered rows.
    """
    upper_triangular_matrix = generate_upper_triangular_matrix_from_rows(rows)
    return upper_triangular_matrix + upper_triangular_matrix.T - numpy.diag(numpy.diagonal(upper_triangular_matrix))


def generate_upper_triangular_matrix_from_rows(rows: List) -> numpy.ndarray:
    """
    Write all rows in a matrix of zeros, aligned to the right, resulting in an upper triangular matrix.

    Args:
        rows: A list of lists, containing the staggered rows of the matrix; that is, the first list has k elements,
        the second list has k-1, and so on.

    Returns:
        A numpy array, representing the matrix which contains the lists of rows right-aligned, and filled with
        zeros in the remaining empty space..
    """
    matrix = numpy.zeros((len(rows), len(rows[0])))
    for i in range(0, len(rows)):
        matrix[i, i:len(rows[0])] = rows[i]
    return matrix


def columns_are_increasing(rows: List) -> bool:
    """
    Checks if all columns of a certain matrix are increasing from a list of lists with increasing elements.
    The growth should not be checked against the rows, as it is expected that the lists forming rows have already
    been generated in increasing order.

    Args:
        rows: A list of lists, containing the staggered rows of the matrix; that is, the first list has k elements,
        the second list has k-1, and so on.

    Returns:
        A boolean, indicating whether the matrix formed by the row vectors of lists, right-aligned and
        filled with zeros in the remaining space, is column-growing.
    """
    upper_triangular_matrix = generate_upper_triangular_matrix_from_rows(rows)

    for i in range(0, len(rows[0])):
        if not numpy.all(numpy.diff(upper_triangular_matrix[0:i + 1, i]) >= 0):
            return False
    return True
