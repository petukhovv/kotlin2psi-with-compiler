import subprocess
import os

from .helpers.TimeLogger import TimeLogger
from .helpers.FilesWalker import FilesWalker
from .helpers.AstHelper import AstHelper


class KotlinSource2AstConverter:
    @staticmethod
    def convert(compiler_path, input_folder, output_folder):
        files_info = {
            'all': 0,
            'current': 0
        }

        def files_count(filename):
            files_info['all'] += 1

        def file_process(filename):
            files_info['current'] += 1

            time_logger = TimeLogger(task_name='Parsing %d of %d file: %s'
                                               % (files_info['current'], files_info['all'], filename))
            subprocess.call([compiler_path, filename])

            relative_filename = os.path.relpath(filename, input_folder)
            output_file = output_folder + '/' + relative_filename
            file_folder = os.path.dirname(output_folder + '/' + relative_filename)
            if not os.path.exists(file_folder):
                os.makedirs(file_folder)

            ast = AstHelper.text2json('ast.data')

            with open(output_file + '.json', 'w') as f:
                f.write(ast)

            time_logger.finish()

        # Count source code files stage
        FilesWalker.walk(input_folder, files_count, extension='kt')

        # Parsing source code files stage
        FilesWalker.walk(input_folder, file_process, extension='kt')
