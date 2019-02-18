import os
import tempfile
import random

class File:

    def __init__(self, filedir):
        self.filedir = filedir


    def write(self, writetext):
        with open(self.filedir, 'a') as f:
            f.write(writetext)

    def read(self):
        with open(self.filedir, 'r') as f:
            return f.read()

    def __add__(self, file):

        with open(os.path.join(tempfile.gettempdir(), str(random.getrandbits(32))+'.txt'), 'w') as new_file:
            new_file.write(self.read())
            new_file.write(file.read())

        return File(new_file.name)

    def __iter__(self):
        return iter(self.read().split('\n'))

    def __str__(self):
        return '{}'.format(self.filedir)
