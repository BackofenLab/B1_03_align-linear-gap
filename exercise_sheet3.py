from helpers.matrix_helpers import nw_init_csv_maker
from typing import Dict, List, Tuple


def exercise_1():
    """
    For the given examples which ones can be called alignments
    Assign the correct boolean value
    """

    # AGTTTTTT
    # AGGTTTTT
    a = None

    # CCGTTTTTT
    # -AGGTTTTT
    b = None

    # CCCGTTTTTTGC
    # -CGGTTTTT
    c = None

    # AG--TTTTTT
    # AG-GTTTTTT
    d = None

    return a, b, c, d


def exercise_2_a():
    """
    Exercise 2 a
    Complete the provided table with the correct initialization step.
    (Hint: Only fill in column 1 and row 1 with the correct values)
    Remember:
                  |  +1 if x = "-" or y = "-"
        w(x,y) =  |  -1 if x = y
                  |  else 0
    """
    row_1 = []
    column_1 = []
    return row_1, column_1


def exercise_2_b():
    """
    Exercise 2 b
    Using dynamic programming technique fill in all values in the matrix.
    (Hint: For column 1 and row 1 you can use the values from exercise 2 a)
     Remember:
                  |  +1 if x = "-" or y = "-"
        w(x,y) =  |  -1 if x = y
                  |  else 0
    """
    #       T  C  C  G  A
    table = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],  # T
        [0, 0, 0, 0, 0, 0],  # A
        [0, 0, 0, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0],  # G
        [0, 0, 0, 0, 0, 0],  # C
        [0, 0, 0, 0, 0, 0],  # G
        [0, 0, 0, 0, 0, 0],  # C
    ]
    return table


def exercise_2_c():
    """
    Exercise 2 c
    Using the matrix from b) find the optimal alignment of the given sequences
     Remember:
                  |  +1 if x = "-" or y = "-"
        w(x,y) =  |  -1 if x = y
                  |  else 0
    """

    sequence1 = "TCCGA"
    sequence2 = "TACGCGC"
    return sequence1, sequence2


def exercise_2_d():
    """
    Exercise 2 d
    Find the optimal alignment of the given sequences, while assuming that the
    first G character in each sequence has to be matched/aligned
    """
    sequence1 = "TCCGA"
    sequence2 = "TACGCGC"
    return sequence1, sequence2


def exercise_3():
    """
    Exercise 3
    Which statements about Needleman-Wunsch and the Hirschberg recursion are
    True and which are False
    """

    # Hirschberg computes global alignment in O(n²) space
    a = None

    # Needleman-Wunsch computes global alignment in O(n²) time
    b = None

    # The Hirschberg recursion is a space optimized version of the
    # Needleman-Wunsch algorithm
    c = None

    # Hirschberg computes global alignment in O(n) time
    d = None
    return a, b, c, d


########################################################
############## Programming tasks #######################
########################################################


def zero_init(seq1, seq2):
    """
    Exercise 4 a
    Implement the function zero_init() which takes two sequences S1 and S2 and
    creates the Needleman-Wunsch matrix and initiates all the matrix values
    with zeroes. Hereby S1 should be represented by the rows and S2 by
    the columns.
    """
    return None


def nw_init(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 b
    Implement the function nw_init() which takes two sequences S1 and S2 as
    well as the scoring function and fills in the values for the first row and
    first column of the matrix with the correct values. Utilize a) in your
    implementation.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )
    matrix = zero_init(seq1, seq2)
    return None


def nw_forward(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 c
    Implement the function nw_forward() which takes the two sequences S1 and
    S2 and the scoring function and output the complete matrix filled with
    the Needleman-Wunsch approach.
    """
    return None


def previous_cells(
    seq1, seq2, scoring, nw_matrix, cell: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Exercise 4 d
    Implement the function previous_cells() which takes two sequences S1 and
    S2, scoring function, the filled in recursion matrix from the step c) and
    the cell coordinates (row, column). The function should output the tuple
    of all possible cell previous cells.
    """
    return None


def build_all_traceback_paths(
    seq1, seq2, scoring, nw_matrix
) -> List[List[Tuple[int, int]]]:
    """
    Exercise 4 e
    Implement the function which builds all possible traceback paths.
    """
    return None


def build_alignment(seq1, seq2, traceback_path) -> Tuple[str, str]:
    """
    Exercise 4 f
    Implement the function build_alignment() which takes two sequences and
    outputs the alignment.
    """
    return None


if __name__ == "__main__":
    """
    You can run this to create csv files from two sequences. Further you can 
    import this file in excel or some similar program, where you can fill in
    the forward values yourself.    
    """
    seq1 = "AT"
    seq2 = "CTAT"
    scoring = {"match": -1, "mismatch": 0, "gap_introduction": 1}

    nw_init_csv_maker(seq1, seq2, scoring)
