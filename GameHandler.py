import random

from Crossword import Crossword
from LoginHandler import LoginHandler


class GameHandler:
    def __init__(self):
        self.loginHandler = LoginHandler()
        self.__playerMenu()

    def __playerMenu(self):
        while True:
            n = int(input("1. One player.\n2. Two player.\n"))
            if n == 1:
                self.__onePlayer()
                break
            else:
                if n == 2:
                    self.__twoPlayer()
                    break
                else:
                    print("Invalid input.")

    def __printPromptsOne(self, playerOne, p1Points):
        print()
        print(f"Player nick:\t{playerOne.nick}\npoints: {p1Points}")
        self.__crossword.wordSet.print()

    def __printPromptsTwo(self, playerOne, p1Points, playerTwo, p2Points):
        print()
        print(f"Player nick:\t{playerOne.nick}\nPoints: {p1Points}")
        print(f"Player nick:\t{playerTwo.nick}\nPoints: {p2Points}")
        self.__crossword.wordSet.print()

    def __mainWordCheck(self):
        if input("Do you want to guess the main word? (y/n)") == "y":
            points = self.__crossword.wordSet.returnNotGuessedNumberOfWordsAndCheckMainWord(input("Input your guess: "))
            return True, points
        else:
            return False, 0

    def __onePlayer(self):
        playerOne = self.loginHandler.getPersonAndPrintMenuPrompt()
        p1Points = 0
        self.__crossword = Crossword()
        while True:
            self.__printPromptsOne(playerOne, p1Points)
            n = self.__getNFromUser()
            userGuess = self.__getUserGuess(n)
            points = self.__crossword.wordSet.words[n].getPointsAndPrintOutcome(userGuess)
            p1Points += points
            if points > 0:
                choice, points = self.__mainWordCheck()
                if choice:
                    if points > 0:
                        p1Points *= points
                        self.__crossword.wordSet.revealAllWords()
                        self.__printPromptsOne(playerOne, p1Points)
                        print(f"Great job!\n{self.__crossword.wordSet.main} - {self.__crossword.wordSet.mainExpl}")
                        break
                    else:
                        print("Unfortunately, incorrect!")
            if self.__crossword.wordSet.isEverythingGuessed():
                break

    def __twoPlayer(self):
        playerOne = self.loginHandler.getPersonAndPrintMenuPrompt()
        p1Points = 0
        playerTwo = self.loginHandler.getPersonAndPrintMenuPrompt()
        p2Points = 0

        if random.randint(0, 1) == 0:
            p = True
        else:
            p = False

        self.__crossword = Crossword()
        while True:
            self.__printPromptsTwo(playerOne, p1Points, playerTwo, p2Points)
            if p:
                print(playerOne.nick, end=" | ")
            else:
                print(playerTwo.nick, end=" | ")
            n = self.__getNFromUser()
            userGuess = self.__getUserGuess(n)
            points = self.__crossword.wordSet.words[n].getPointsAndPrintOutcome(userGuess)
            if p:
                p1Points += points
            else:
                p2Points += points
            if points > 0:
                choice, points = self.__mainWordCheck()
                if choice:
                    if points > 0:
                        if p:
                            p1Points *= points
                        else:
                            p2Points *= points
                        self.__crossword.wordSet.revealAllWords()
                        self.__printPromptsTwo(playerOne, p1Points, playerTwo, p2Points)
                        print(f"Great job!\n{self.__crossword.wordSet.main} - {self.__crossword.wordSet.mainExpl}")
                        break
                    else:
                        print("Unfortunately, incorrect!")
            else:
                p = not p
            if self.__crossword.wordSet.isEverythingGuessed():
                break

    def __getUserGuess(self, n):
        self.__crossword.wordSet.words[n].printClue()
        userGuess = input("Please input your guess: ")
        return userGuess

    def __getNFromUser(self):
        while True:
            try:
                n = int(input("Which word do you want to guess? "))
                if self.__crossword.wordSet.words[n-1].canGuess:  # 0 < n <= len(self.__crossword.wordSet.words) and
                    break
                else:
                    print("This word has already been guessed.")
            except ValueError:
                print("Invalid input try again.")
            except IndexError:
                print("Invalid input try again.")
        return n-1
