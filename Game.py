from LoginHandler import LoginHandler


class Game:
    def __init__(self):
        n = self.__getHowManyPlayersAndPrintPrompts()
        self.loginHandler = LoginHandler()
        if n == 1:
            self.__onePlayer()
        if n == 2:
            self.__doublePlayer()

    @staticmethod
    def __getHowManyPlayersAndPrintPrompts():
        while True:
            n = input("1 or 2 players?")
            if n == 1 or n == 2:
                break
            else:
                print("Invalid input.")
        return n

    def __onePlayer(self):
        self.__playerOne = self.loginHandler.getPersonAndPrintMenuPrompt()

    def __doublePlayer(self):
        self.__playerOne = self.loginHandler.getPersonAndPrintMenuPrompt()
        self.__playerTwo = self.loginHandler.getPersonAndPrintMenuPrompt()
