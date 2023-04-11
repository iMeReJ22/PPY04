class Word:
    def __init__(self, passwd, startPosition, mainIndex, clue):
        self.__passwd = "" + passwd
        self.__startPosition = int(startPosition)
        self.__toGuess = list()
        self.__mainIndex = int(mainIndex)+1
        self.__clue = clue
        self.canGuess = True
        for i in range(len(passwd)):
            self.__toGuess.append("_")

    def printClue(self):
        print(self.__clue)

    def printWord(self):
        for i in range(self.__startPosition):
            print(end=" ")
        for i in range(len(self.__passwd)):
            if i == self.__mainIndex:
                print("]", end="")
            if i == self.__mainIndex-1:
                print("[", end="")
            print(self.__toGuess[i], end="")
        print()

    def revealWord(self):
        self.__toGuess = self.__passwd

    def getPointsAndPrintOutcome(self, guess):
        if guess == self.__passwd or guess == self.__passwd.lower():
            pts = len(self.__passwd)
            self.__toGuess = self.__passwd
            print(f"Great choice, you get {pts} points.")
            self.canGuess = False
            return pts
        else:
            pts = -len(self.__passwd)
            print(f"Wrong choice! You lose {pts} points.")
            return pts




