class Word:
    def __init__(self, passwd, startPosition, mainIndex, clue):
        self.passwd = "" + passwd
        self.startPosition = startPosition
        self.toGuess = list()
        self.mainIndex = mainIndex
        self.clue = clue
        for i in range(len(passwd)):
            self.toGuess.append("_")

    def printWord(self):
        for i in range(self.startPosition):
            if i == self.mainIndex:
                print("[", end="")
            if i == self.mainIndex-1:
                print("]", end="")
            print("_", end="")
        print(self.toGuess)

    def getPointsAndPrintOutcome(self, guess):

        if guess == self.passwd or guess == self.passwd.lower():
            pts = len(self.passwd)
            self.toGuess = self.toGuess
            print(f"Great choice, you get {pts} points.")
            return pts
        else:
            print("Wrong choice!")
            return 0




