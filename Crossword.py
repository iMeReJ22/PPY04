from WordSet import WordSet


class Crossword:
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

    @staticmethod
    def __getWordSets():
        wordSets = list()
        wordSets.append(WordSet("Plants", "germination", {
            "growth": "Process of increasing in physical size, mass, volume, or number of cells.",
            "tree": "Plant with a single stem or trunk, supporting branches and leaves above the ground.",
            "herbs": "Plants that are used for medicinal, culinary, or aromatic purposes.",
            "stamen": "The male reproductive organ of a flower, consisting of a filament and an anther.",
            "vines": "Plants with long, slender stems that grow along the ground or climb up and wrap around other objects or plants for support.",
            "beans": "A type of legume that are commonly consumed as a food.",
            "leaves": "Flattened, usually green structures that are attached to the stem of a plant.",
            "trowel": "Small handheld tool with a flat, pointed blade that is used for digging, spreading, and smoothing materials.",
            "mildew": "Type of fungus that can grow on surfaces, such as walls, fabrics, and plants.",
            "tomatoes": "Typically round or oblong in shape and come in a variety of colors, including red, yellow, and green.",
            "orange": "What color are marigold flowers?"
        }))

        return wordSets

