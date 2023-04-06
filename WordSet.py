class WordSet:
    def __init__(self, theme, main, side):
        self.theme = theme
        self.main = main
        self.side = side
        self.guessed = 0
    def print(self):
        print(f"{self.theme: }")
        for i in range(len(self.side)):
            print()