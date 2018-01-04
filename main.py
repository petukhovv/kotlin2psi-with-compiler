import argparse

from lib.KotlinSource2AstConverter import KotlinSource2AstConverter
from lib.helpers.TimeLogger import TimeLogger


parser = argparse.ArgumentParser()
parser.add_argument('--compiler_path', '-c', nargs=1, type=str, help='path to custom version of kotlin compiler')
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with kotlin source codes')
parser.add_argument('--output_folder', '-o', nargs=1, type=str, help='output folder with AST as JSON')

kt_code_temp_file = 'code.kt'

args = parser.parse_args()
compiler_path = args.compiler_path[0]
input_folder = args.input_folder[0]
output_folder = args.output_folder[0]

time_logger = TimeLogger()

KotlinSource2AstConverter.convert(compiler_path, input_folder, output_folder)

time_logger.finish(task_name='Parsing')
