import os
import tempfile


class File:

    def __init__(self, full_path):

        self.full_path = full_path

    def write(self, str_to_write):

        with open(self.full_path, 'w') as f:

            f.write(str_to_write)

    def __add__(self, obj):

        # Creating new file in /tmp

        new_file_path = os.path.join(tempfile.gettempdir(), 'result.txt')

        # Writing content of file1 in result file

        with open(new_file_path, 'w') as result:

            with open(self.full_path, 'r') as file1:

                file1_content = file1.read()

            result.write(file1_content)

        # Adding content of file2 in result file

        with open(new_file_path, 'a') as result:

            with open(obj.full_path, 'r') as file2:

                file2_content = file2.read()

            result.write(file2_content)

        return File(new_file_path)

    def __str__(self):
        return self.full_path

    def __getitem__(self, index):

        with open(self.full_path, 'r') as f:

            f_cont = f.readlines()

        return f_cont[index]
