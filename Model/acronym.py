class Acronym:
    def __init__(self, word):
        self.word = word

    def createAcronym(self):
        acronym = self.word.split()
        abb = ""
        length = len(acronym)

        for i in range(0, length):
            abb += acronym[i][0].upper()

        print(abb)