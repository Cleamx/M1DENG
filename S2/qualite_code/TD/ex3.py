import random

def division(a, b):
    return a / b

for _ in range(100):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    try:
        print(f"{a} / {b} = {division(a, b)}")
    except ZeroDivisionError:
        print(f"{a} / {b} = division par zéro")