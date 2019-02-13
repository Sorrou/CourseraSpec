class FileReader():
    def __init__(self, mafile):
        self.mafile = mafile

    def read(self):
        try:
            file = open(self.mafile, mode='r')
            return file.read()
        except IOError:
            return ""

def main():
    x = FileReader('D:\\123.txt')
    print(x.read())

if __name__ == "__main__":
    main()
