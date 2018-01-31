from .lib.KotlinSource2AstConverter import KotlinSource2AstConverter
from .lib.helpers.TimeLogger import TimeLogger


kt_code_temp_file = 'code.kt'
compiler_path = './lib/kotlinc/bin/kotlinc'


def source2ast(input_folder, output_folder):
    time_logger = TimeLogger()

    KotlinSource2AstConverter.convert(compiler_path, input_folder, output_folder)

    time_logger.finish(task_name='Parsing')
