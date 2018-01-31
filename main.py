import argparse

from lib.KotlinSource2AstConverter import KotlinSource2AstConverter
from lib.helpers.TimeLogger import TimeLogger


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with kotlin source codes')
parser.add_argument('--output_folder', '-o', nargs=1, type=str, help='output folder with AST as JSON')

kt_code_temp_file = 'code.kt'
compiler_path = './lib/kotlinc/bin/kotlinc'

args = parser.parse_args()
input_folder = args.input_folder[0]
output_folder = args.output_folder[0]

time_logger = TimeLogger()

KotlinSource2AstConverter.convert(compiler_path, input_folder, output_folder)

time_logger.finish(task_name='Parsing')
