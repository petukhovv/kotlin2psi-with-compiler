import subprocess
import os

from .helpers.TimeLogger import TimeLogger
from .helpers.FilesWalker import FilesWalker
from .helpers.AstHelper import AstHelper


class KotlinSource2AstConverter:
    folder = 'ast'

    @staticmethod
    def convert(compiler_path, input_folder, output_folder):
        params = {'counter': 1}

        def file_process(filename, params):
            time_logger = TimeLogger()
            subprocess.call([compiler_path, filename])

            relative_filename = os.path.relpath(filename, input_folder)
            output_file = output_folder + '/' + relative_filename
            file_folder = os.path.dirname(output_folder + '/' + relative_filename)
            if not os.path.exists(file_folder):
                os.makedirs(file_folder)

            ast = AstHelper.text2json('ast.data')

            with open(output_file + '.json', 'w') as f:
                f.write(ast)

            print(str(params['counter']) + ' parse completed. Parsing time:' + str(time_logger.finish()))

            params['counter'] += 1

        FilesWalker.walk(input_folder, lambda file: file_process(file, params))
