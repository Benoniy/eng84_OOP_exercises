

class ScrabbleCalc:

    def __init__(self):
        # Dictionary that contains letter and their scores
        self.letter_vals = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                            "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                            "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                            "y": 4, "z": 10
                            }
        self.word = ""  # For storing the original word
        self.score = 0  # Tracks the score of a word

    # Used to calculate the score of a word
    def calculate_score(self, word):
        self.word = word  # Store the original
        lower = word.lower().strip()  # Format the word for processing

        # Loop through the word and add the score for each char
        for char in lower:
            self.score += self.letter_vals[char]

        # Print the value of the word
        print(f"{word} is worth {self.score} points!")
        self.reset_calc()

    # Reset the score and word for next time
    def reset_calc(self):
        self.word = ""
        self.score = 0


if __name__ == "__main__":
    calc = ScrabbleCalc()
    calc.calculate_score("antidisestablishmentarianism")
