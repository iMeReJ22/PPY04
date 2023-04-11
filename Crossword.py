import os
import random
import re

from WordSet import WordSet


class Crossword:
    def __init__(self):
        self.wordSet = self.__getWordSetAndPrintPrompts()

    def __getWordSetAndPrintPrompts(self):
        wordSets = self.__getWordSets()
        for i in range(len(wordSets)):
            print(f"{i+1}. {wordSets[i].theme}.")
        return wordSets[self.__getIndexOfChosenWordSet(wordSets)]

    @staticmethod
    def __getIndexOfChosenWordSet(wordSets):
        while True:
            try:
                n = input("Chose your crossword theme: ('r' for random)")
                if n == "r":
                    n = random.randint(0, len(wordSets))
                else:
                    n = int(n)
                if n <= 0 or n > len(wordSets):
                    raise ValueError
                else:
                    return n-1
            except ValueError:
                print("Invalid input, try again.")

    def __getWordSets(self):
        wordSets = list()
        files = self.__getFiles()
        for file in files:
            wordSets.append(WordSet(file))
        return wordSets

    @staticmethod
    def __getFiles():
        wordSetFiles = list()
        files = os.listdir("Data")
        for file in files:
            pattern = re.compile("^wordSet.*\\.txt$")
            if pattern.match(file):
                wordSetFiles.append(file)

        return wordSetFiles

