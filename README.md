# OOP exercises:
## 01 - Fizzbuzz:
1. To acheive oop fizzbuzz I created a class FizzBuzz
```python
class FizzBuzz:

    def __init__(self):
        self.fizz = 3  # divisible by number for fizz
        self.buzz = 5  # divisible by number for buzz
```
2. I then added methods that could detect if a number was fizz or buzz.
```python
    # Checks if a number is fizz
    def is_fizz(self, value):
        return value % self.fizz == 0

    # Checks if a number is buzz
    def is_buzz(self, value):
        return value % self.buzz == 0
```
3. I created a method that used those two methods to determine if a number was fizzbuzz.
```python
    # Checks if a number is fizz and is buzz
    def is_fizz_buzz(self, value):
        return self.is_fizz(value) and self.is_buzz(value)
```
4. Finally I created a method that generated 1 to 100 and implements these methods.
```python
    # Generates 1 to 100 in order and checks if they are fizz or buzz using the object methods
    def gen_100(self):
        for num in range(1, 101, 1):  # loop from 1 to 100
            if self.is_fizz_buzz(num):  # is it fizz and buzz?
                print("fizzbuzz")
            elif self.is_buzz(num):  # is it buzz?
                print("buzz")
            elif self.is_fizz(num):  # is it fizz?
                print("fizz")
            else:  # is it none of the above?
                print(num)
```
5. To use this class:
````python
    fizz_buzz = FizzBuzz()
    fizz_buzz.gen_100()
````
## 02 - Scrabble word calculator:
1. To satisfy the requirements provided for this program I created a class ScrabbleCalc,  
I decided to use a dictionary to store the values of each letter and progress from there.
```python
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
```
2. I then created a method that would use these instance variables to calculate and store  
the value of a word
```python
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
```
3. Finally I created a method that would reset the object so that it could be used again
```python
    # Reset the score and word for next time
    def reset_calc(self):
        self.word = ""
        self.score = 0
```
4. To use this class:
```python
    calc = ScrabbleCalc()
    calc.calculate_score("word")
```
