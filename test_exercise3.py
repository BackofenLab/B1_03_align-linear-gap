def init_matrix(seq1, seq2):
    return [[0] * (len(seq2)+1) for i in range(len(seq1) + 1)]


def nw_init(seq1, seq2, scoring):
    match, mismatch, gap = scoring
    matrix = init_matrix(seq1, seq2)
    first_row = [i * mismatch for i in range(len(seq2) + 1)]
    matrix[0] = first_row
    for index, column in enumerate(matrix):
        column[0] = index * mismatch
    return matrix


def matrix_to_csv(seq1, seq2, matrix, csv_file_name="matrix.csv"):
    with open(csv_file_name, "w") as f:
        f.write(",".join("  "+seq2) + "\n")

        left_column = " " + seq1
        for index, char in enumerate(left_column):
            f.write(char + "," + ",".join([str(x) for x in matrix[index]]) + "\n")


if __name__ == "__main__":
    seq1 = "AT"
    seq2 = "CTAT"
    scoring = (1, -2, -1)

    matrix = nw_init(seq1, seq2, scoring)
    for row in matrix:
        print(row)
    matrix_to_csv(seq1, seq2, matrix)
