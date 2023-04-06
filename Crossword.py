import os
import re

from Word import Word
from WordSet import WordSet


class Crossword:
    def __init__(self):
        wordSet = self.__getWordSetAndPrintPrompts()

    def __getWordSetAndPrintPrompts(self):
        wordSets = self.__getWordSets()
        for i in range(len(wordSets)):
            print(f"{i}. {wordSets[i].theme}.")
        return wordSets[self.__getIndexOfChosenWordSet(wordSets)]

    @staticmethod
    def __getIndexOfChosenWordSet(wordSets):
        while True:
            try:
                n = int(input("Chose your crossword theme: "))
                if n <= 0 or n > len(wordSets):
                    raise ValueError
                else:
                    return n
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

