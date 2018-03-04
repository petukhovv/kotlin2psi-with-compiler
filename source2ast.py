import os

from lib.KotlinSource2AstConverter import KotlinSource2AstConverter
from lib.helpers.TimeLogger import TimeLogger


kt_code_temp_file = 'code.kt'
current_folder = os.path.dirname(os.path.abspath(__file__))
compiler_path = '%s/lib/kotlinc/bin/kotlinc' % current_folder


def source2ast(input_folder, output_folder):
    time_logger = TimeLogger(task_name='Parsing')

    KotlinSource2AstConverter.convert(compiler_path, input_folder, output_folder)

    time_logger.finish(full_finish=True)
