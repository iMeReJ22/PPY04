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
                self.main = parts[0]
                self.mainExpl = parts[1]
                self.theme = parts[2]

            else:
                self.words.append(Word(parts[0], parts[1], parts[2], parts[3]))

    def revealAllWords(self):
        for w in self.words:
            w.revealWord()

    def returnNotGuessedNumberOfWordsAndCheckMainWord(self, guess):
        if self.main == guess:
            i = 0
            for w in self.words:
                if w.canGuess:
                    i += 1
            return i
        else:
            return -len(self.main)

    def isEverythingGuessed(self):
        for i in self.words:
            if i.canGuess:
                return False
        return True

    def print(self):
        print(f"Theme: {self.theme:}")
        for i in range(len(self.words)):
            print(end=f"{i+1}.\t\t")
            self.words[i].printWord()
