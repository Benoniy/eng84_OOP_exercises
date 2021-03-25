

class ScrabbleCalc:

    def __init__(self):
        self.letter_vals = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                            "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                            "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                            "y": 4, "z": 10
                            }
        self.word = ""
        self.score = 0

    def calculate_score(self, word):
        self.word = word
        lower = word.lower().strip()

        for char in lower:
            self.score += self.letter_vals[char]

        print(f"{word} is worth {self.score} points!")
        self.reset_calc()

    def reset_calc(self):
        self.word = ""
        self.score = 0


if __name__ == "__main__":
    calc = ScrabbleCalc()
    calc.calculate_score("antidisestablishmentarianism")
