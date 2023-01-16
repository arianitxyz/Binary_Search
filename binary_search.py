class BinarySearch(object):

    def __init__(self):
        self.answer = 1
        self.low = 1
        self.high = 100

    def search(self) -> int:
        tries = 0
        if self.answer not in range(self.low, self.high):
            return 0
        while self.low <= self.high:
            guess = self.low + (self.high - self.low) // 2
            if guess < self.answer:
                self.low = guess + 1
                tries += 1
            elif guess > self.answer:
                self.high = guess - 1
                tries += 1
            else:
                tries += 1
                return tries
