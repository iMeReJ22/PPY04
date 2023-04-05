class Word:
    def __init__(self, passwd, startPosition, mainIndex):
        self.passwd = passwd
        self.startPosition = startPosition
        self.toGuess = list()
        self.mainIndex = mainIndex
        for i in range(len(passwd)):
            self.toGuess.append("_")

    def printWord(self):
        for i in range(self.startPosition):
            if i == self.mainIndex or i == self.mainIndex-1:
                print("|", end="")
            print(" ", end="")
        print(self.toGuess)

    def getPointsAndPrintOutcome(self, guess):
        if guess == self.passwd:
            pts = len(self.passwd)
            self.toGuess = self.toGuess
            print(f"Great choice, you get {pts} points.")
            return pts
        else:
            print("Wrong choice!")
            return 0




