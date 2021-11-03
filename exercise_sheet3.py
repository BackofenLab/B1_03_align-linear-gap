from helpers.matrix_helpers import nw_init_csv_maker


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



def init_zero(seq1, seq2):
    return None


if __name__ == "__main__":
    seq1 = "AT"
    seq2 = "CTAT"
    scoring = {"match": 1,
               "mismatch": -2,
               "gap_introduction": -1}


    nw_init_csv_maker(seq1, seq2, scoring)
