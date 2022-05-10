# This program is Fibonacci's serie but it´s generates using a iterator
import time

class Fibonacci():
    def __init__(self, max = 5):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.counter += 1
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 =self.aux
                # Using swaping from python
                self.n1, self.n2 = self.n2, self.aux
                return self.aux
        else:
            raise StopIteration


if __name__ == '__main__':
    fibonacci = Fibonacci()

    for element in fibonacci:
        print(element)
        time.sleep(0.5)
