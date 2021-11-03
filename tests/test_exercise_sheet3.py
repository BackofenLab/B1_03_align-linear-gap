from exercise_sheet3 import *
from helpers.matrix_helpers import nw_init, given_matrix_csv_maker


def test_exercise_1a():
    a, b, c, d = exercise_1()
    assert a


def test_exercise_1b():
    a, b, c, d = exercise_1()
    assert b


def test_exercise_1c():
    a, b, c, d = exercise_1()
    assert not c


def test_exercise_1d():
    a, b, c, d = exercise_1()
    assert d


def test_exercise_2a():
    row, column = exercise_2_a()
    assert row == [0, 1, 2, 3, 4, 5]
    assert column == [0, 1, 2, 3, 4, 5, 6, 7]


def test_exercise_2b():
    expected_table = [
        [0,  1,  2,  3,  4,  5],
        [1, -1,  0,  1,  2,  3],
        [2,  0, -1,  0,  1,  1],
        [3,  1, -1, -2, -1,  0],
        [4,  2,  0, -1, -3, -2],
        [5,  3,  1, -1, -2, -3],
        [6,  4,  2,  0, -2, -2],
        [7,  5,  3,  1, -1, -2],
    ]
    table = exercise_2_b()
    assert expected_table == table


def test_exercise_2c():
    sequence1, sequence2 = exercise_2_c()
    assert sequence1 == "T-C-CGA"
    assert sequence2 == "TACGCGC"


def test_exercise_2d():
    """
    Hint: w(a*, b*) = sum_i(w(a_i, b_i))
    """
    sequence1, sequence2 = exercise_2_d()
    assert sequence1 in ["TCCGA--", "TCCG-A-", "TCCG--A"]
    assert sequence2 == "TACGCGC"


def test_exercise_3():
    a, b, c, d = exercise_3()
    assert not a
    assert b
    assert c
    assert not d


def test_exercise_3a():
    a, b, c, d = exercise_3()
    assert not a


def test_exercise_3b():
    a, b, c, d = exercise_3()
    assert b


def test_exercise_3c():
    a, b, c, d = exercise_3()
    assert c


def test_exercise_3d():
    a, b, c, d = exercise_3()
    assert not d


def nw_forward(seq1, seq2, scoring):
    matrix = nw_init(seq1, seq2, scoring)
    match_score, mismatch_score, gap_score = scoring["match"], scoring["mismatch"], scoring["gap_introduction"]

    for row_index, row in enumerate(matrix[1:], 1):
        for column_index, column in enumerate(row[1:], 1):
            char_seq_1, char_seq_2 = seq1[row_index-1], seq2[column_index-1]
            no_gap_score = match_score if char_seq_1 == char_seq_2 else mismatch_score

            diagonal = matrix[row_index-1][column_index-1] + no_gap_score
            left = matrix[row_index][column_index - 1] + gap_score
            top = matrix[row_index - 1][column_index] + gap_score
            max_val = max(top, left, diagonal)
            matrix[row_index][column_index] = max_val

    return matrix


if __name__ == "__main__":
    seq1 = "AT"
    seq2 = "CTAT"
    scoring = {"match": 1,
               "mismatch": -2,
               "gap_introduction": -1}

    matrix = nw_init(seq1, seq2, scoring)
    matrix = nw_forward(seq1, seq2, scoring)
    given_matrix_csv_maker(seq1, seq2, matrix)
