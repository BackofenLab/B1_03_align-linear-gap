from helpers.matrix_helpers import matrix_to_csv


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


    matrix_to_csv(seq1, seq2, scoring)
