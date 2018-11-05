#!/usr/bin/env python3
class FileReader:
        """Класс FileReader помогает читать из файла"""

        def __init__(self, path):
            self.path = path

        def read(self):
            try:
                with open(self.path, 'r') as f:

                    result = f.read()

                return result
            except IOError:
                return ""


