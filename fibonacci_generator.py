# This program is an implementation of Fibonacci's series, using generator.
import time

# Generator are sugar sintax for iterators. They are functions

def fibonacci_gener(max:int = 5):
    max = max
    n1 = 0
    n2 = 1
    counter = 0

    while counter < max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux


if __name__ == '__main__':
    fibonacci = fibonacci_gener()

    for element in fibonacci:
        print(element)
        time.sleep(0.5)
    