import argparse

from source2ast import source2ast

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with kotlin source codes')
parser.add_argument('--output_folder', '-o', nargs=1, type=str, help='output folder with AST as JSON')
parser.add_argument('--with_code', action='store_true', help='whether to write the source code in CST')

args = parser.parse_args()
input_folder = args.input_folder[0]
output_folder = args.output_folder[0]
with_code = args.with_code

source2ast(input_folder, output_folder, with_code)
