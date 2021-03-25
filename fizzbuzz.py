

class FizzBuzz:

    def __init__(self):
        self.fizz = 3  # divisible by number for fizz
        self.buzz = 5  # divisible by number for buzz

    # Checks if a number is fizz
    def is_fizz(self, value):
        return value % self.fizz == 0

    # Checks if a number is buzz
    def is_buzz(self, value):
        return value % self.buzz == 0

    # Checks if a number is fizz and is buzz
    def is_fizz_buzz(self, value):
        return self.is_fizz(value) and self.is_buzz(value)

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


if __name__ == "__main__":
    fizz_buzz = FizzBuzz()
    fizz_buzz.gen_100()
