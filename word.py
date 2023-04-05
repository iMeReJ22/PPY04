class word:
    def __init__(self, passwd, startPosition, mainIndex):
        self.passwd = passwd
        self.startPosition = startPosition
        self.toGuess = list()
        self.mainIndex = mainIndex
        for i in range(len(passwd)):
            self.toGuess.append("_")

    def replaceLetterAndReturnPoints(self, letter):
        toReplace = list(self.toGuess)
        pts = 0
        for i in range(len(toReplace)):
            if letter == self.passwd[i]:
                pts += 1
                toReplace[i] = letter
        self.toGuess = listToString(toReplace)

    def printWord(self):
        for i in range(self.startPosition):
            print(" ", end="")
        print(self.toGuess)
            


def listToString(list):
    tmp = ""
    for ch in list:
        tmp += ch
    return tmp

