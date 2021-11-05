import argparse
from helpers.matrix_helpers import nw_init_csv_maker


parser = argparse.ArgumentParser(description='Parameters for the NW')
parser.add_argument('--first', type=str,
                    help='first sequence')
parser.add_argument('--second', type=str,
                    help='second sequence')

parser.add_argument('--match', type=int,
                    help='match score')

parser.add_argument('--mismatch', type=int,
                    help='mismatch score')

parser.add_argument('--gap_introduction', type=int,
                    help='gap introduction score')


parser.add_argument('--file_name', type=str, default="matrix.csv",
                    help='file name')


args = parser.parse_args()

seq_first = args.first
seq_second = args.second

match = args.match
mismatch = args.mismatch
gap = args.gap_introduction

file_name = args.file_name

scoring = {"match": match, "mismatch": mismatch, "gap_introduction": gap}


nw_init_csv_maker(seq_first, seq_second, scoring, file_name)
