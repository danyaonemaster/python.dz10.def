import math


def calc_a(a):
    if a == 0:
        raise Exception("A - should not be zero")
    return ((a ** 4) * math.pi + 100) / a


def calc_b(b):
    if b == 0:
        raise Exception("B - should not be zero")
    return (((b ** 3) + 100) * math.pi) / b ** 2


input_a = int(input("Enter is number a :"))
input_b = int(input("Enter is number b :"))
print(f"{round(calc_a(input_a), 2)} - {round(calc_b(input_b), 2)} = {round(calc_a(input_a) - calc_b(input_b), 2)}")
