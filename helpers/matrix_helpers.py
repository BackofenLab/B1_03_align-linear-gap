def zero_init_correct(seq1, seq2):
    return [[0] * (len(seq2)+1) for _ in range(len(seq1) + 1)]


def nw_init_correct(seq1, seq2, scoring):
    match, mismatch, gap = scoring["match"], scoring["mismatch"], scoring["gap_introduction"]
    matrix = zero_init_correct(seq1, seq2)
    first_row = [i * mismatch for i in range(len(seq2) + 1)]
    matrix[0] = first_row
    for index, column in enumerate(matrix):
        column[0] = index * mismatch
    return matrix


def nw_init_csv_maker(seq1, seq2, scoring, csv_file_name="matrix.csv"):
    matrix = nw_init_correct(seq1, seq2, scoring)
    with open(csv_file_name, "w") as f:
        f.write(",".join("  "+seq2) + "\n")

        left_column = " " + seq1
        for index, char in enumerate(left_column):
            f.write(char + "," + ",".join([str(x) for x in matrix[index]]) + "\n")


def given_matrix_csv_maker(seq1, seq2, matrix, csv_file_name):
    with open(csv_file_name, "w") as f:
        f.write(",".join("  "+seq2) + "\n")

        left_column = " " + seq1
        for index, char in enumerate(left_column):
            f.write(char + "," + ",".join([str(x) for x in matrix[index]]) + "\n")


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
            min_val = min(top, left, diagonal)
            matrix[row_index][column_index] = min_val
    return matrix