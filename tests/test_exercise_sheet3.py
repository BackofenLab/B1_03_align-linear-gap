import sys
from exercise_sheet3 import *
from helpers.matrix_helpers import nw_init_csv_maker, given_matrix_csv_maker


def test_exercise_1():
    a, b, c, d = exercise_1()
    assert a
    assert b
    assert not c
    assert not d


def test_exercise_2_a():
    row, column = exercise_2_a()
    assert row == [0, 1, 2, 3, 4, 5]
    assert column == [0, 1, 2, 3, 4, 5, 6, 7]


def test_exercise_2_b():
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


def test_exercise_2_c():
    sequence1, sequence2 = exercise_2_c()
    assert sequence1 == "T-C-CGA"
    assert sequence2 == "TACGCGC"


def test_exercise_2_d():
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


###############################################
###########Programming related tests###########
###############################################


def init_matrix_correct(seq1, seq2):
    return [[0] * (len(seq2)+1) for _ in range(len(seq1) + 1)]


def nw_init_correct(seq1, seq2, scoring):
    match, mismatch, gap = scoring["match"], scoring["mismatch"], scoring["gap_introduction"]
    matrix = init_matrix_correct(seq1, seq2)
    first_row = [i * gap for i in range(len(seq2) + 1)]
    matrix[0] = first_row
    for index, column in enumerate(matrix):
        column[0] = index * gap
    return matrix


def nw_forward_correct(seq1, seq2, scoring):
    matrix = nw_init_correct(seq1, seq2, scoring)
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


def previous_cells_correct(seq1, seq2, scoring, nw_matrix, cell):
    prev_cells = []
    row, column = cell

    top = (row - 1, column) if row > 0 else None
    left = (row, column - 1) if column > 0 else None
    diagonal = (row - 1, column - 1) if (row > 0 and column > 0) else None

    cur_val = nw_matrix[row][column]
    char_first, char_second = seq1[row-1], seq2[column-1]
    match_score = scoring["match"] if char_first == char_second else scoring["mismatch"]
    gap_score = scoring["gap_introduction"]

    if diagonal:
        diagonal_val = nw_matrix[diagonal[0]][diagonal[1]]
        if (diagonal_val + match_score) == cur_val:
            prev_cells.append(diagonal)

    if top:
        top_val = nw_matrix[top[0]][top[1]]
        if (top_val + gap_score) == cur_val:
            prev_cells.append(top)

    if left:
        left_val = nw_matrix[left[0]][left[1]]
        if (left_val + gap_score) == cur_val:
            prev_cells.append(left)

    return prev_cells


def build_all_traceback_paths_correct(seq1, seq2, scoring, nw_matrix):
    list_traceback_paths = []

    cell = len(nw_matrix) - 1, len(nw_matrix[0]) - 1
    frontier = [[cell]]
    while frontier:
        partial_path = frontier.pop()
        last_cell_partial = partial_path[-1]
        next_steps = previous_cells_correct(seq1, seq2, scoring, nw_matrix, last_cell_partial)
        for next_step in next_steps:
            new_traceback_path = partial_path + [next_step]
            if next_step == (0, 0):
                list_traceback_paths.append(new_traceback_path)
            else:
                frontier.append(new_traceback_path)

    return list_traceback_paths


def build_alignment_correct(seq1, seq2, alignment_path):
    align_seq1 = ''
    align_seq2 = ''

    alignment_path = alignment_path[::-1]

    prev_cell = 0, 0
    for cell in alignment_path[1:-1]:
        prev_row, prev_column = prev_cell
        row, column = cell

        if (row > prev_row) and (column > prev_column):
            align_seq1 += seq1[row-1]
            align_seq2 += seq2[column-1]

        elif row > prev_row:
            align_seq1 += seq1[row-1]
            align_seq2 += "-"

        else:
            align_seq1 += "-"
            align_seq2 += seq2[column-1]

        prev_cell = cell

    return align_seq1, align_seq2


def check_implementation():
    sequence1 = "ATACGAC"
    sequence2 = "TTACGGACCCC"
    scoring = {"match": 1,
               "mismatch": -2,
               "gap_introduction": -1}

    matrix = nw_forward_correct(sequence1, sequence2, scoring)
    given_matrix_csv_maker(sequence1, sequence2, matrix, "nw_matrix_test.csv")
    all_traceback_paths = build_all_traceback_paths_correct(sequence1, sequence2, scoring, matrix)

    for tr in all_traceback_paths:
        al1, al2 = build_alignment_correct(sequence1, sequence2, tr)

        print(al1)
        print(al2)
        print("\n")


if __name__ == "__main__":
    check_implementation()



