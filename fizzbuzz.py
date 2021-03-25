

class FizzBuzz:

    def __init__(self):
        self.fizz = 3
        self.buzz = 5

    def is_fizz(self, value):
        return value % self.fizz == 0

    def is_buzz(self, value):
        return value % self.buzz == 0

    def is_fizz_buzz(self, value):
        return self.is_fizz(value) and self.is_buzz(value)

    def gen_100(self):
        for num in range(1, 101, 1):
            if self.is_fizz_buzz(num):
                print("fizzbuzz")
            elif self.is_buzz(num):
                print("buzz")
            elif self.is_fizz(num):
                print("fizz")

            else:
                print(num)


if __name__ == "__main__":
    fizz_buzz = FizzBuzz()
    fizz_buzz.gen_100()
