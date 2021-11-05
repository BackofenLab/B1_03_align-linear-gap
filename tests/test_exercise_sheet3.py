from exercise_sheet3 import *
import pytest
import pprint
from helpers.matrix_helpers import (
    nw_init_correct,
    given_matrix_csv_maker,
    nw_forward_correct,
    zero_init_correct,
    build_all_traceback_paths_correct,
    previous_cells_correct,
    build_alignment_correct,
)

SCORING = [
    {"match": -1, "mismatch": 0, "gap_introduction": 1},
    {"match": -1, "mismatch": 0, "gap_introduction": 2},
    {"match": -1, "mismatch": 1, "gap_introduction": 2},
    {"match": -1, "mismatch": 2, "gap_introduction": 1},
]


def test_exercise_1a():
    a, b, c, d = exercise_1()
    assert a is True


def test_exercise_1b():
    a, b, c, d = exercise_1()
    assert b is True


def test_exercise_1c():
    """
    In an alignment both strings have to be of same length
    """
    a, b, c, d = exercise_1()
    assert c is False


def test_exercise_1d():
    """
    A gap cannot be aligned with a gap
    """
    a, b, c, d = exercise_1()
    assert d is False


def test_exercise_2a():
    row, column = exercise_2_a()
    assert row == [0, 1, 2, 3, 4, 5]
    assert column == [0, 1, 2, 3, 4, 5, 6, 7]


def test_exercise_2b():
    expected_table = [
        [0, 1, 2, 3, 4, 5],
        [1, -1, 0, 1, 2, 3],
        [2, 0, -1, 0, 1, 1],
        [3, 1, -1, -2, -1, 0],
        [4, 2, 0, -1, -3, -2],
        [5, 3, 1, -1, -2, -3],
        [6, 4, 2, 0, -2, -2],
        [7, 5, 3, 1, -1, -2],
    ]
    table = exercise_2_b()
    assert expected_table == table


def test_exercise_2c():
    sequence1, sequence2 = exercise_2_c()
    assert sequence1 == "TACGCGC"
    assert sequence2 == "T-C-CGA"


def test_exercise_2d():
    """
    Hint: w(a*, b*) = sum_i(w(a_i, b_i))
    You can split the alignment at the G and treat it as two separate
    alignments
    """
    sequence1, sequence2 = exercise_2_d()
    assert sequence1 == "TACGCGC"
    assert sequence2 in ["TCCGA--", "TCCG-A-", "TCCG--A"]


def test_exercise_3a():
    a, b, c, d = exercise_3()
    assert a is False


def test_exercise_3b():
    a, b, c, d = exercise_3()
    assert b is True


def test_exercise_3c():
    a, b, c, d = exercise_3()
    assert c is True


def test_exercise_3d():
    a, b, c, d = exercise_3()
    assert d is False


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC")
    ]
)
def test_exercise_4a(seq1, seq2):
    expected_matrix = zero_init_correct(seq1, seq2)
    actual_matrix = zero_init(seq1, seq2)
    if actual_matrix != expected_matrix:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your matrix is:")
        pprint.pprint(actual_matrix)
        print("It is supposed to look like:")
        pprint.pprint(expected_matrix)
    assert expected_matrix == actual_matrix


@pytest.mark.parametrize(
    "seq1,seq2,scoring",
    [
        ("TCCGA", "TACGCGC", SCORING[0]),
        ("TCCGA", "TACGCGC", SCORING[1]),
        ("TCCGA", "TACGCGC", SCORING[2]),
    ]
)
def test_exercise_4b(seq1, seq2, scoring):
    expected_matrix = nw_init_correct(seq1, seq2, scoring)
    actual_matrix = nw_init(seq1, seq2, scoring)
    if actual_matrix != expected_matrix:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your matrix is:")
        pprint.pprint(actual_matrix)
        print("It is supposed to look like:")
        pprint.pprint(expected_matrix)
    assert expected_matrix == actual_matrix


@pytest.mark.parametrize(
    "seq1,seq2,scoring",
    [
        ("TCCGA", "TACGCGC", SCORING[0]),
        ("TCCGA", "TACGCGC", SCORING[1]),
        ("TCCGA", "TACGCGC", SCORING[2]),
    ]
)
def test_exercise_4c(seq1, seq2, scoring):
    expected_matrix = nw_forward_correct(seq1, seq2, scoring)
    actual_matrix = nw_forward(seq1, seq2, scoring)
    if actual_matrix != expected_matrix:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your matrix is:")
        pprint.pprint(actual_matrix)
        print("It is supposed to look like:")
        pprint.pprint(expected_matrix)
    assert expected_matrix == actual_matrix

@pytest.mark.parametrize(
    "seq1,seq2,scoring,cell",
    [
        ("TCCGA", "TACGCGC", SCORING[0], (1, 1)),
        ("TCCGA", "TACGCGC", SCORING[1], (5, 7)),
        ("TCCGA", "TACGCGC", SCORING[2], (3, 4)),
    ]
)
def test_exercise_4d(seq1, seq2, scoring, cell):
    nw_matrix = nw_forward_correct(seq1, seq2, scoring)
    expected_cells = previous_cells_correct(
        seq1, seq2, scoring, nw_matrix, cell
    )
    actual_cells = previous_cells(seq1, seq2, scoring, nw_matrix, cell)
    expected_cells = set(expected_cells)
    actual_cells = set(actual_cells)
    if actual_cells != expected_cells:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\ncell: {cell}\n"
              f"scoring: {scoring}")
        print(f"Your previous cells are:\n{actual_cells}")
        print(f"It should be:\n{expected_cells}")
    assert expected_cells == actual_cells


@pytest.mark.parametrize(
    "seq1,seq2,scoring",
    [
        ("TCCGA", "TACGCGC", SCORING[0]),
        ("TCCCGG", "TCAAA", SCORING[0]),
        ("TCCGA", "TACGCGC", SCORING[1]),
        ("TCCGA", "TACGCGC", SCORING[2]),
        ("AAA", "TTT", SCORING[3]),

    ]
)
def test_exercise_4e(seq1, seq2, scoring):
    nw_matrix = nw_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, nw_matrix
    )
    actual_paths = build_all_traceback_paths(seq1, seq2, scoring, nw_matrix)
    expected_paths = [tuple(x) for x in expected_paths]
    expected_paths = set(expected_paths)
    actual_paths = [tuple(x) for x in actual_paths]
    actual_paths = set(actual_paths)
    if actual_paths != expected_paths:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your paths are:")
        pprint.pprint(actual_paths)
        print(f"It should be:")
        pprint.pprint(expected_paths)
    assert expected_paths == actual_paths


@pytest.mark.parametrize(
    "seq1,seq2,scoring",
    [
        ("TCCGA", "TACGCGC", SCORING[0]),
        ("TCCCGG", "TCAAA", SCORING[0]),
        ("TCCGA", "TACGCGC", SCORING[1]),
        ("TCCGA", "TACGCGC", SCORING[2]),
        ("AAA", "TTT", SCORING[3]),
    ]
)
def test_exercise_4f(seq1, seq2, scoring):
    nw_matrix = nw_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, nw_matrix
    )
    for traceback_path in expected_paths:
        expected_alignment = build_alignment_correct(seq1, seq2, traceback_path)
        actual_alignment = build_alignment(seq1, seq2, traceback_path)
        if actual_alignment != expected_alignment:
            print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}\npath: {traceback_path}")
            print("Your alignment is:")
            print(f"S1: {actual_alignment[0]}\nS2: {actual_alignment[1]}")
            print("It should be:")
            print(f"S1: {expected_alignment[0]}\nS2: {expected_alignment[1]}")
        assert expected_alignment == actual_alignment


if __name__ == "__main__":
    seq1 = "AT"
    seq2 = "CTAT"

    scoring = {"match": -1, "mismatch": 0, "gap_introduction": 1}

    matrix = nw_forward_correct(seq1, seq2, scoring)
    given_matrix_csv_maker(seq1, seq2, matrix, "correct_matrix.csv")
