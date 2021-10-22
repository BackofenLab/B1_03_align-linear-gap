def init_matrix(seq1, seq2):
    return [[0] * (len(seq2)+1) for i in range(len(seq1) + 1)]


def nw_init(seq1, seq2, scoring):
    match, mismatch, gap = scoring["match"], scoring["mismatch"], scoring["gap_introduction"]
    matrix = init_matrix(seq1, seq2)
    first_row = [i * mismatch for i in range(len(seq2) + 1)]
    matrix[0] = first_row
    for index, column in enumerate(matrix):
        column[0] = index * mismatch
    return matrix


def nw_init_csv_maker(seq1, seq2, scoring, csv_file_name="matrix.csv"):
    matrix = nw_init(seq1, seq2, scoring)
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


