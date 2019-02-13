class FileReader():
    def __init__(self, mafile):
        self.mafile = mafile

    def read(self):
        try:
            file = open(self.mafile, mode='r')
            return file.read()
        except IOError:
            return ""
