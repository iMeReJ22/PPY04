from Word import Word


class WordSet:
    def __init__(self, path):
        self.__initDataFromFile(path)

    def __initDataFromFile(self, path):
        file = open(f"Data/{path}")
        self.words = list()
        first = True
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if first:
                first = False
                self.theme = parts[0]
                self.main = parts[1]
            else:
                self.words.append(Word(parts[0], parts[1], parts[2], parts[3]))

    def print(self):
        print(f"{self.theme: }")
        for i in range(len(self.words)):
            print()